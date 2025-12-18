"""
Exemplo mínimo de uso do TIR (mostra como passar caminho customizado de config.json)

Observação: o nome do pacote pode ser `tir_framework` (instalado pelo pip). O exemplo tenta importar ambos os nomes comuns.
"""
import os

def import_tir():
    try:
        import tir_framework as tir
        return tir
    except Exception:
        try:
            import tir as tir
            return tir
        except Exception as e:
            raise ImportError("Não foi possível importar 'tir_framework' nem 'tir' - instale o pacote no venv") from e


def main():
    tir = import_tir()
    # ajuste o caminho conforme seu arquivo config.json
    cfg_path = os.path.join(os.getcwd(), "config.json")
    print("Usando config:", cfg_path)

    # Exemplo ilustrativo: criação de uma instância Webapp (a API real depende do pacote)
    try:
        Webapp = getattr(tir, 'Webapp', None)
        if Webapp is None:
            print("A biblioteca importada não expõe 'Webapp' — verifique a API do pacote.")
            return
        helper = Webapp(cfg_path)
        print("Instância Webapp criada:", helper)
    except Exception as e:
        print("Erro ao instanciar Webapp:", e)


if __name__ == '__main__':
    main()
