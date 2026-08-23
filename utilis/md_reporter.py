import os
import json
import time
import glob
import tempfile
import traceback
from datetime import datetime

# Carimbo de versão. Se este print não aparecer no console ao rodar o teste,
# o Python NÃO está carregando este arquivo (há outra cópia sendo usada,
# ou o arquivo em utilis/md_reporter.py não foi realmente sobrescrito).
VERSION = "md_reporter v3 - reports/index (2026-08-22)"
print(f"[md_reporter] carregado: {VERSION} | arquivo: {os.path.abspath(__file__)}")


# Raiz de todos os relatórios: docs/reports, ao lado do projeto (caminho absoluto,
# baseado na localização deste arquivo — nunca no cwd, que pode mudar durante os testes).
_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.abspath(os.path.join(_BASE_DIR, ".."))
REPORTS_ROOT = os.path.join(_PROJECT_ROOT, "docs", "reports")


def _escrever_atomico(caminho, conteudo):
    """Escreve o arquivo de forma atômica: grava em um temp e substitui no final.
    Evita arquivo corrompido/parcial se o processo for interrompido no meio da escrita."""
    pasta = os.path.dirname(caminho)
    fd, temp_path = tempfile.mkstemp(dir=pasta, prefix=".tmp_", suffix=".swap")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(conteudo)
        os.replace(temp_path, caminho)  # atômico no mesmo filesystem
    except Exception:
        if os.path.exists(temp_path):
            os.remove(temp_path)
        raise


class TirReportAgent:
    """Proxy para interceptar chamadas do TIR e gerar relatório consolidado em Markdown,
    organizado por módulo dentro de docs/reports/.

    - Cada teste é identificado por uma chave única: self.nome_teste.
    - Os resultados de TODOS os testes de um módulo ficam em um único resultados.json,
      indexado por essa chave. Rodar o mesmo teste de novo SOBRESCREVE a entrada.
    - O .md do módulo é sempre REGERADO por completo a partir do JSON — nunca editado
      via regex. Isso é o que garante zero duplicação.
    - Ao final, atualiza também um índice geral (docs/reports/index.md) com o resumo
      de todos os módulos, para o time acompanhar de forma centralizada.
    """

    def _categoria(self, nome_metodo):
        # Mapeamento baseado nos métodos realmente usados no TIR (sem "Click" genérico,
        # que não é utilizado neste framework). SetLateralMenu não entra aqui porque
        # não é contado — o caminho da rotina é capturado à parte (ver __getattr__).
        if nome_metodo == "SetButton":
            return "cliques"        # Clique ou confirmação
        if nome_metodo == "WaitShow":
            return "validacoes"     # Validação de tela/mensagem esperada
        if nome_metodo == "SetValue":
            return "insercoes"      # Inserção ou alteração de campo
        if nome_metodo == "GetValue":
            return "leituras"       # Leitura de campo
        if nome_metodo.startswith("Screenshot"):
            return "screenshots"
        return None

    def __init__(self, tir_instance, cod_modulo, nome_modulo, ct_nome, descricao):
        self._oHelper = tir_instance
        self.modulo = cod_modulo
        self.nome_modulo = nome_modulo
        self.nome_teste = ct_nome.strip()
        self.descricao = descricao
        self.start_time = time.time()
        self.status = "PASSOU"
        self.erro = None

        self.contadores = {
            "cliques": 0,
            "validacoes": 0,
            "insercoes": 0,
            "leituras": 0,
            "screenshots": 0,
        }
        self.caminho_rotina = None

        # Pasta do módulo: "07_Gestao_de_Pessoal" (código + nome, mais fácil de navegar)
        nome_pasta = f"{self.modulo}_{self.nome_modulo}".replace(" ", "_")
        self.dir_modulo = os.path.join(REPORTS_ROOT, nome_pasta)
        os.makedirs(self.dir_modulo, exist_ok=True)

        self.arquivo_dados = os.path.join(self.dir_modulo, "resultados.json")
        self.arquivo_relatorio = os.path.join(self.dir_modulo, "Relatorio_Consolidado.md")

        # Log de diagnóstico: se algum dia duplicar de novo, isso mostra exatamente
        # em qual arquivo físico está gravando — cole essa linha se precisar investigar.
        print(f"[TirReportAgent] JSON: {self.arquivo_dados}")
        print(f"[TirReportAgent] MD:   {self.arquivo_relatorio}")

    def __getattr__(self, name):
        attr = getattr(self._oHelper, name)
        if callable(attr):
            def wrapper(*args, **kwargs):
                if name == "SetLateralMenu" and args:
                    # Guarda o caminho real da rotina, ex: "Atualizações > Cadastros > Funções"
                    self.caminho_rotina = args[0]
                categoria = self._categoria(name)
                if categoria:
                    self.contadores[categoria] += 1
                return attr(*args, **kwargs)
            return wrapper
        return attr

    def registrar_erro(self, e):
        self.status = "FALHOU"
        self.erro = traceback.format_exc()

    # ---------- Persistência ----------

    def _carregar_dados(self):
        if os.path.exists(self.arquivo_dados):
            with open(self.arquivo_dados, "r", encoding="utf-8") as f:
                try:
                    bruto = json.load(f)
                except json.JSONDecodeError:
                    return {}
            # normaliza chaves (defesa extra contra espaços/maiúsculas escondidas)
            return {k.strip(): v for k, v in bruto.items()}
        return {}

    # ---------- Renderização ----------

    def _render_bloco(self, nome_teste, info):
        emoji = "🟩" if info["status"] == "PASSOU" else "🟥"
        arquivo_teste = nome_teste if nome_teste.endswith(".py") else f"{nome_teste}.py"

        # O ">" usado como separador no caminho da rotina (ex: "Atualizações > Cadastros")
        # conflita com a sintaxe de blockquote do Markdown (linha começando com "> ").
        # Trocamos só na exibição por "›", que é visualmente equivalente e não quebra o preview.
        rotina = str(info.get("caminho_rotina", "-")).replace(" > ", " › ")

        linhas = [
            "<details>",
            f"<summary><b>{emoji} {info['status']} | <code>{arquivo_teste}</code> — "
            f"{info['descricao']}</b> (⏱️ {info['duracao']:.2f}s)</summary>",
            "<br>",
            "",
            f"> **Rotina:** {rotina}",
            f"> **Última Execução:** {info['data_hora']} | **Resultado:** `{info['status']}`",
            "",
            "* **📊 Métricas do Teste:**",
            f"  * **Cliques/Confirmações:** `{info['contadores'].get('cliques', 0)}`",
            f"  * **Validações:** `{info['contadores'].get('validacoes', 0)}`",
            f"  * **Inserções/Alterações:** `{info['contadores'].get('insercoes', 0)}`",
            f"  * **Leitura de Campos:** `{info['contadores'].get('leituras', 0)}`",
            f"  * **Screenshots/Prints:** `{info['contadores'].get('screenshots', 0)}`",
            f"  * **Tempo de Execução:** `{info['duracao']:.2f} segundos`",
        ]
        if info.get("erro"):
            linhas.append("  * **❌ Detalhes da Falha:**")
            linhas.append("  ```text")
            linhas.append(info["erro"].rstrip())
            linhas.append("  ```")
        linhas += ["", "</details>", "", "---", ""]
        return "\n".join(linhas)

    def salvar_relatorio(self):
        duration = time.time() - self.start_time

        # 1) Atualiza (sobrescreve) SOMENTE a entrada deste teste
        dados = self._carregar_dados()
        dados[self.nome_teste] = {
            "status": self.status,
            "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "duracao": duration,
            "descricao": self.descricao,
            "caminho_rotina": self.caminho_rotina or "-",
            "contadores": self.contadores,
            "erro": self.erro,
        }
        _escrever_atomico(self.arquivo_dados, json.dumps(dados, ensure_ascii=False, indent=2))

        # 2) Regera o .md do módulo inteiro a partir do JSON
        passou = sum(1 for v in dados.values() if v["status"] == "PASSOU")
        falhou = len(dados) - passou

        linhas = [
            "# 📑 Relatório de Execução de Testes",
            f"### Módulo {self.modulo} - {self.nome_modulo}",
            "",
            f"**Resumo:** {len(dados)} teste(s) · 🟩 {passou} passou(aram) · 🟥 {falhou} falhou(aram)",
            "",
            "---",
            "",
        ]
        for nome_teste, info in dados.items():
            linhas.append(self._render_bloco(nome_teste, info))

        _escrever_atomico(self.arquivo_relatorio, "\n".join(linhas))

        # 3) Atualiza o índice geral (visão para o time)
        atualizar_indice_geral()


def atualizar_indice_geral():
    """Varre docs/reports/*/resultados.json e gera um índice geral (index.md)
    com o resumo de cada módulo. Pode ser chamado isoladamente também,
    por exemplo ao final de um pipeline de CI que roda vários módulos."""
    os.makedirs(REPORTS_ROOT, exist_ok=True)
    jsons = sorted(glob.glob(os.path.join(REPORTS_ROOT, "*", "resultados.json")))

    linhas = [
        "# 📊 Painel Geral de Testes — TIR Protheus",
        "",
        f"_Atualizado em {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}_",
        "",
        "| Módulo | Testes | 🟩 Passou | 🟥 Falhou | Última Execução | Relatório |",
        "| --- | --- | --- | --- | --- | --- |",
    ]

    for caminho_json in jsons:
        pasta_modulo = os.path.basename(os.path.dirname(caminho_json))
        with open(caminho_json, "r", encoding="utf-8") as f:
            dados = json.load(f)

        if not dados:
            continue

        passou = sum(1 for v in dados.values() if v["status"] == "PASSOU")
        falhou = len(dados) - passou
        ultima = max(
            (v["data_hora"] for v in dados.values()),
            key=lambda s: datetime.strptime(s, "%d/%m/%Y %H:%M:%S"),
        )
        link_relativo = f"{pasta_modulo}/Relatorio_Consolidado.md"

        linhas.append(
            f"| {pasta_modulo} | {len(dados)} | {passou} | {falhou} | {ultima} | [Abrir]({link_relativo}) |"
        )

    _escrever_atomico(os.path.join(REPORTS_ROOT, "index.md"), "\n".join(linhas) + "\n")