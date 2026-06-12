import re
import os
import base64
from datetime import datetime

def imagem_para_base64(caminho_imagem):
    """Converte uma imagem em string Base64 para ser incorporada no HTML."""
    # Tenta localizar a imagem no diretório atual ou subpastas comuns
    if not os.path.exists(caminho_imagem):
        # Se não achar o caminho puro, tenta adicionar .png se faltar
        if not caminho_imagem.lower().endswith('.png'):
            caminho_imagem += '.png'
    
    if os.path.exists(caminho_imagem):
        with open(caminho_imagem, "rb") as img_file:
            b64 = base64.b64encode(img_file.read()).decode('utf-8')
            return f"data:image/png;base64,{b64}"
    return None

def gerar_guia_homologacao(caminho_arquivo_teste):
    """Gera um guia de homologação visual na pasta C:\Relatorios_Homologacao."""
    if not os.path.exists(caminho_arquivo_teste):
        return

    with open(caminho_arquivo_teste, 'r', encoding='utf-8') as f:
        conteudo = f.read()
        linhas = conteudo.splitlines()

    # Dicionário para mapear variáveis do código (ex: self.filial -> '02DF0001')
    variaveis_valor = {}
    atribuicoes = re.findall(r"(?:self|cls)\.(\w+)\s*=\s*['\"](.*?)['\"]", conteudo)
    for var, valor in atribuicoes:
        variaveis_valor[var] = valor

    nome_arquivo = os.path.basename(caminho_arquivo_teste)
    diretorio_origem = os.path.dirname(caminho_arquivo_teste)
    
    # Alteração: Caminho público para que qualquer pessoa possa acessar
    diretorio_saida = r"C:\Relatorios_Homologacao"
    if not os.path.exists(diretorio_saida):
        os.makedirs(diretorio_saida)

    nome_teste = nome_arquivo.replace('.py', '')
    display_test_name = nome_teste.replace('test_', '').replace('_', ' ').title()
    
    passos = []
    pre_requisitos = []
    objetivo_doc = "Validar a execução da rotina e integridade dos dados no Protheus."

    # Tenta extrair o objetivo do comentário inicial do arquivo
    for linha in linhas:
        if "class" in linha and ":" in linha: break
        clean_line = linha.strip().replace('#', '').replace('-', '').strip()
        if linha.strip().startswith('#') and len(clean_line) > 10 and "Importa" not in clean_line:
            objetivo_doc = clean_line
            break

    for linha in linhas:
        linha_limpa = linha.strip()
        
        # Identificar Pré-requisitos (variáveis no setUpClass)
        if 'self.filial' in linha or 'cls.filial' in linha:
            res = re.search(r"=\s*['\"](.*?)['\"]", linha)
            if res: pre_requisitos.append(f"Filial: {res.group(1)}")
        elif 'cls.dataref' in linha or 'self.dataref' in linha:
            pre_requisitos.append("Data de Referência (Data Base do sistema)")
            
        # 1. Menu Lateral
        if '.SetLateralMenu(' in linha_limpa:
            res = re.search(r'SetLateralMenu\([\'"](.*?)[\'"]\)', linha_limpa)
            if res: passos.append(f"Acesse o menu principal do Protheus e navegue seguindo o caminho: <strong>{res.group(1)}</strong>")
            
        # 2. Execução de Programa
        elif '.Program(' in linha_limpa:
            res = re.search(r'Program\([\'"](.*?)[\'"]\)', linha_limpa)
            if res: passos.append(f"Inicie a rotina técnica do sistema executando o programa/transação: <strong>{res.group(1)}</strong>")

        # 3. Preenchimento de Campos (SetValue)
        elif '.SetValue(' in linha_limpa:
            # Regex para pegar o nome do campo e o valor (tratando aspas e argumentos extras)
            res = re.search(r'SetValue\(\s*[\'"](.*?)[\'"]\s*,\s*([^,\)]*)', linha_limpa)
            if res:
                # Remove o "?" que costuma vir nos campos de parâmetros do Protheus
                campo = res.group(1).replace('?', '').strip()
                valor_raw = res.group(2).strip().replace('self.', '').replace('cls.', '').strip("'\"")
                
                # Tenta traduzir a variável para o valor real
                valor_final = variaveis_valor.get(valor_raw, valor_raw)
                if valor_raw == 'DateSystem':
                    valor_final = datetime.today().strftime('%d/%m/%Y')
                
                passos.append(f"Localize o campo de entrada <strong>'{campo}'</strong> e preencha-o com a informação: <code>{valor_final}</code>")
                
        # 4. Clique em Botões
        elif '.SetButton(' in linha_limpa:
            res = re.search(r"SetButton\(\s*['\"](.*?)['\"]", linha_limpa)
            if res: passos.append(f"Acione o botão <strong>'{res.group(1)}'</strong> para confirmar a ação ou prosseguir para a próxima etapa.")

        # 5. Aguardar Tela
        elif '.WaitShow(' in linha_limpa:
            res = re.search(r"WaitShow\(['\"](.*?)['\"]", linha_limpa)
            if res: passos.append(f"Certifique-se de que o sistema carregou e exibiu corretamente a tela de <strong>{res.group(1)}</strong> antes de continuar.")

        # 6. Validação de Resultados
        elif '.CheckResult(' in linha_limpa:
            res = re.search(r"CheckResult\(['\"](.*?)['\"]\s*,\s*['\"](.*?)['\"]", linha_limpa)
            if res:
                campo_val = res.group(1).replace('?', '').strip()
                passos.append(f"<span style='color:#d32f2f'>➔ <strong>Validação Crucial:</strong></span> Verifique se o conteúdo do campo <strong>'{campo_val}'</strong> corresponde exatamente a: <code>{res.group(2)}</code>")

        # 7. Captura de Tela (Evidência)
        elif '.Screenshot(' in linha_limpa:
            res = re.search(r"Screenshot\(['\"](.*?)['\"]", linha_limpa)
            if res:
                img_name = res.group(1)
                caminho_img = os.path.join(diretorio_origem, img_name if img_name.lower().endswith('.png') else img_name + '.png')
                b64_data = imagem_para_base64(caminho_img)
                if b64_data:
                    passos.append(f"<div style='margin-top:15px; background:#f9f9f9; padding:10px; border-radius:8px; text-align:center; border:1px solid #eee;'><p style='font-size:12px; color:#666;'>📸 Evidência Visual: {img_name}</p><img src='{b64_data}' style='max-width:100%; border-radius:4px; box-shadow:0 2px 10px rgba(0,0,0,0.1);'></div>")
                else:
                    passos.append(f"📸 <em>Verificar evidência salva como: {img_name}.png</em>")

        # 8. Seleção de Checkbox/Grid
        elif '.ClickBox(' in linha_limpa:
            res = re.search(r"ClickBox\(['\"](.*?)['\"]", linha_limpa)
            if res: passos.append(f"Na listagem de dados (Grid), localize e selecione o registro que contém a informação: <strong>{res.group(1)}</strong>")

    # Template HTML
    html = f"""
<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="windows-1252">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Homologação - {display_test_name}</title>

    <style>

        :root {{
            --primary: #005a92;
            --primary-light: #eaf4fb;
            --success: #198754;
            --warning: #ffc107;
            --danger: #dc3545;
            --purple: #6f42c1;

            --background: #f4f6f9;
            --card: #ffffff;
            --border: #dde2e7;

            --text: #333;
            --text-light: #666;

            --shadow: 0 3px 10px rgba(0,0,0,0.06);
            --radius: 10px;
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', Arial, sans-serif;
            background: var(--background);
            color: var(--text);
            line-height: 1.7;
            padding: 30px;
        }}

        .container {{
            max-width: 1200px;
            margin: auto;
        }}

        /* ===================================================
           HEADER
        =================================================== */

        header {{
            background: linear-gradient(135deg, #005a92, #0078c2);
            color: white;
            padding: 35px;
            border-radius: var(--radius);
            margin-bottom: 25px;
            box-shadow: var(--shadow);
        }}

        header h1 {{
            font-size: 32px;
            margin-bottom: 10px;
        }}

        header p {{
            opacity: 0.95;
            font-size: 16px;
        }}

        .badge {{
            display: inline-block;
            background: rgba(255,255,255,0.15);
            padding: 6px 12px;
            border-radius: 20px;
            margin-top: 10px;
            font-size: 13px;
        }}

        /* ===================================================
           CARDS
        =================================================== */

        .card {{
            background: var(--card);
            border-radius: var(--radius);
            padding: 25px;
            margin-bottom: 25px;
            box-shadow: var(--shadow);
            border: 1px solid var(--border);
        }}

        h2 {{
            color: var(--primary);
            font-size: 24px;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #edf1f5;
        }}

        h3 {{
            margin-bottom: 10px;
        }}

        p {{
            margin-bottom: 12px;
        }}

        strong {{
            color: #222;
        }}

        /* ===================================================
           INFO GRID
        =================================================== */

        .info-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 15px;
            margin-top: 20px;
        }}

        .info-box {{
            background: var(--primary-light);
            padding: 18px;
            border-left: 5px solid var(--primary);
            border-radius: 8px;
        }}

        .info-box strong {{
            display: block;
            margin-bottom: 5px;
            color: var(--primary);
        }}

        /* ===================================================
           STATS
        =================================================== */

        .stats {{
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            margin-top: 20px;
        }}

        .stat {{
            flex: 1;
            min-width: 180px;
            background: #f8fafc;
            border: 1px solid var(--border);
            padding: 20px;
            border-radius: 8px;
            text-align: center;
        }}

        .stat .number {{
            display: block;
            font-size: 28px;
            font-weight: bold;
            color: var(--primary);
        }}

        .stat .label {{
            color: var(--text-light);
            font-size: 14px;
        }}

        /* ===================================================
           PRE REQUISITOS
        =================================================== */

        .pre-req-list {{
            list-style: none;
            margin-top: 15px;
        }}

        .pre-req-list li {{
            background: #fff9e6;
            border-left: 5px solid var(--warning);
            padding: 14px;
            border-radius: 6px;
            margin-bottom: 10px;
        }}

        /* ===================================================
           PASSOS
        =================================================== */

        .steps-list {{
            list-style: none;
            counter-reset: step;
        }}

        .steps-list li {{
            position: relative;
            background: #fafbfd;
            border: 1px solid #e6ebf0;
            border-radius: 10px;
            padding: 20px 20px 20px 75px;
            margin-bottom: 16px;
            transition: all 0.2s ease;
        }}

        .steps-list li:hover {{
            background: #f4f9fd;
            transform: translateY(-1px);
        }}

        .steps-list li::before {{
            counter-increment: step;
            content: counter(step);

            position: absolute;
            left: 20px;
            top: 18px;

            width: 38px;
            height: 38px;

            border-radius: 50%;
            background: var(--primary);

            color: white;
            font-weight: bold;

            display: flex;
            align-items: center;
            justify-content: center;
        }}

        /* ===================================================
           TIPOS DE PASSO
        =================================================== */

        .validation {{
            border-left: 5px solid var(--success);
            background: #f1fbf5 !important;
        }}

        .evidence {{
            border-left: 5px solid var(--purple);
            background: #f6f3ff !important;
        }}

        .warning {{
            border-left: 5px solid var(--warning);
            background: #fffdf2 !important;
        }}

        .tag {{
            display: inline-block;
            padding: 4px 10px;
            font-size: 11px;
            border-radius: 20px;
            margin-bottom: 10px;
            font-weight: 600;
        }}

        .tag-validation {{
            background: #daf5e5;
            color: #146c43;
        }}

        .tag-evidence {{
            background: #ece5ff;
            color: #5a3ea5;
        }}

        /* ===================================================
           CODE
        =================================================== */

        code {{
            background: #eef1f5;
            padding: 3px 8px;
            border-radius: 5px;
            color: #c7254e;
            font-family: Consolas, monospace;
            font-size: 14px;
        }}

        /* ===================================================
           TABLE
        =================================================== */

        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
        }}

        table th {{
            background: var(--primary);
            color: white;
            padding: 12px;
            text-align: left;
        }}

        table td {{
            padding: 12px;
            border: 1px solid var(--border);
        }}

        /* ===================================================
           FOOTER
        =================================================== */

        footer {{
            text-align: center;
            margin-top: 40px;
            color: var(--text-light);
            font-size: 13px;
        }}

        /* ===================================================
           RESPONSIVO
        =================================================== */

        @media (max-width: 768px) {{

            body {{
                padding: 15px;
            }}

            header {{
                padding: 25px;
            }}

            header h1 {{
                font-size: 24px;
            }}

            .steps-list li {{
                padding-left: 65px;
            }}

            .stats {{
                flex-direction: column;
            }}
        }}

    </style>

</head>

<body>

<div class="container">

    <header>
        <h1>Guia de Homologação</h1>

        <p style="font-size: 18px; margin-top: 5px;">
            Processo: <strong>{display_test_name}</strong>
        </p>

        <span class="badge">
            Documento gerado automaticamente
        </span>
    </header>

    <section class="card">

        <h2>1. Visão Geral</h2>

        <p>
            Este documento descreve os passos necessários para a validação
            funcional da rotina <strong>{display_test_name}</strong>.
        </p>

        <div class="info-grid">

            <div class="info-box">
                <strong>Objetivo</strong>
                {objetivo_doc}
            </div> 

            <div class="info-box">
                <strong>Tipo</strong>
                Teste funcional automatizado
            </div>

            <div class="info-box">
                <strong>Plataforma</strong>
                Protheus / TIR
            </div>

        </div>

    </section>

    <section class="card">

        <h2>2. Pré-requisitos</h2>

        <ul class="pre-req-list">

            <li>
                ✅ Ambiente Protheus ativo e acessível.
            </li>

            <li>
                ✅ Usuário com permissões adequadas para as rotinas envolvidas.
            </li>

            {"".join([f"<li><strong>{item}</strong></li>" for item in pre_requisitos])}

        </ul>

    </section>

    <section class="card">

        <h2>3. Estatísticas do Teste</h2>

        <div class="stats">

            <div class="stat">
                <span class="number">{len(passos) if passos else 0}</span>
                <span class="label">Passos Identificados</span>
            </div>

            <div class="stat">
                <span class="number">{sum(1 for p in passos if 'Validação Crucial' in p) if passos else 0}</span>
                <span class="label">Validações</span>
            </div>

            <div class="stat">
                <span class="number">{sum(1 for p in passos if '📸' in p) if passos else 0}</span>
                <span class="label">Evidências</span>
            </div>

        </div>

    </section>

    <section class="card">

        <h2>4. Guia de Execução</h2>

        <ol class="steps-list">
            {"" if passos else "<li>Nenhuma ação de sistema detectada no script de teste.</li>"}
            {
                "".join([
                    f'''
                    <li class="
                        {"validation" if "Validação Obrigatória" in p else ""}
                        {"evidence" if "evidência" in p.lower() else ""}
                    ">
                        {
                            '<span class="tag tag-validation">VALIDAÇÃO</span>'
                            if "Validação Obrigatória" in p else ''
                        }

                        {
                            '<span class="tag tag-evidence">EVIDÊNCIA</span>'
                            if "evidência" in p.lower() else ''
                        }

                        {p}
                    </li>
                    '''
                    for p in passos
                ])
            }

        </ol>

    </section>

    <section class="card">

        <h2>5. Resultados Esperados</h2>

        <table style="margin-bottom: 20px;">

            <thead>
                <tr>
                    <th>Critério</th>
                    <th>Resultado Esperado</th>
                </tr>
            </thead>

            <tbody>

                <tr>
                    <td>Fluxo do Processo</td>
                    <td>Concluído sem interrupções inesperadas ou mensagens de erro críticas.</td>
                </tr>

                <tr>
                    <td>Validações Específicas</td>
                    <td>Todos os pontos de "Validação Crucial" devem apresentar o resultado esperado, conforme indicado no passo a passo.</td>
                </tr>

                <tr>
                    <td>Integridade dos Dados</td>
                    <td>As informações inseridas/alteradas devem ser gravadas corretamente no banco de dados do Protheus e refletidas nas consultas pertinentes.</td>
                </tr>
                <tr>
                    <td>Evidências Visuais</td>
                    <td>As telas do sistema devem corresponder às capturas de tela fornecidas, garantindo a conformidade visual e funcional.</td>
                </tr>
                <tr>
                    <td>Mensagens do Sistema</td>
                    <td>Mensagens de sucesso, avisos ou logs de ocorrência devem ser exibidos conforme o comportamento padrão da rotina.</td>
                </tr>

            </tbody>

        </table>
        
        <div class="card" style="background-color: var(--primary-light); border-color: var(--primary); margin-top: 30px;">
            <h3 style="color: var(--primary); margin-top: 0;">6. Parecer de Aprovação</h3>
            <p>Após a execução e verificação de todos os passos e critérios acima, o processo será considerado <strong>HOMOLOGADO</strong> se:</p>
            <ul>
                <li>Não houver divergências funcionais ou visuais.</li>
                <li>Todos os resultados esperados forem confirmados.</li>
                <li>A integridade dos dados for mantida.</li>
            </ul>
            <p style="margin-top: 20px; font-size: 14px; color: var(--text-light);">
                <strong>Homologador:</strong> _____________________________________________ 
                <strong>Data:</strong> ____/____/____
            </p>
        </div>

    </section>

    <footer>

        Guia de Homologação gerado automaticamente em
        {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}

    </footer>

</div>

</body>

</html>
"""
    
    caminho_html = os.path.join(diretorio_saida, f"Guia_Homologacao_{nome_teste}.html")
    # Salvando com o encoding windows-1252 solicitado
    with open(caminho_html, 'w', encoding='cp1252', errors='replace') as f: # Mantém o encoding cp1252
        f.write(html)
    
    print(f"--- Guia de Homologação Didático Criado: {caminho_html} ---")