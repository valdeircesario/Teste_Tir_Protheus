# Projeto de Automação de Testes TIR - Protheus

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![TIR Framework](https://img.shields.io/badge/TIR-2.4.3-green.svg)](https://totvs.github.io/tir/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Este é um projeto pessoal de desenvolvimento e demonstração de automação de testes funcionais para aplicações Totvs Protheus Webapp, utilizando o framework TIR (Totvs Interface Robot). O objetivo é apresentar habilidades em automação de testes, desenvolvimento de scripts de teste e configuração de ambientes de teste.

## 📋 Sumário

- [Sobre o Projeto](#sobre-o-projeto)
- [Pré-requisitos](#pré-requisitos)
- [Instalação e Setup](#instalação-e-setup)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Executando Testes](#executando-testes)
- [Configuração](#configuração)
- [Logs e Debug](#logs-e-debug)
- [Comandos Úteis](#comandos-úteis)
- [Troubleshooting](#troubleshooting)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Licença](#licença)

## 🎯 Sobre o Projeto

Este projeto demonstra a implementação de testes automatizados para sistemas Protheus, cobrindo:

- ✅ **Setup completo** de ambiente de desenvolvimento
- ✅ **Testes funcionais** com operações CRUD
- ✅ **Interação com grids** e formulários web
- ✅ **Captura de valores dinâmicos** gerados pelo sistema
- ✅ **Relatórios de execução** e logs detalhados
- ✅ **Configuração flexível** para diferentes ambientes

Ideal para portfólio de desenvolvedor, apresentações técnicas ou como base para projetos de automação de testes.

## 🔧 Pré-requisitos

Antes de começar, certifique-se de ter os seguintes softwares instalados:

### 1. Python 3.12
- **Versão recomendada**: Python 3.12.10 ou superior
- **Download**: [Site oficial do Python](https://www.python.org/downloads/)
- **Instalação**: Durante a instalação, marque a opção "Add Python to PATH"
- **Verificação**:
  ```powershell
  python --version
  ```
  Deve mostrar: `Python 3.12.10`

### 2. Git (opcional, para clonar repositórios)
- **Download**: [Site oficial do Git](https://git-scm.com/downloads)
- **Verificação**:
  ```powershell
  git --version
  ```

### 3. Acesso a Ambiente Protheus
- Ambiente de teste Protheus Webapp acessível
- Credenciais válidas para o ambiente
- Conexão de rede estável

## 🚀 Instalação e Setup

### Passo 1: Obter o Projeto

**Opção A: Clonar via Git**
```powershell
git clone https://github.com/valdeircesario/Teste_Tir_Protheus.git
cd Teste_Tir_Protheus
```

**Opção B: Download Manual**
- Baixe o arquivo ZIP do repositório
- Extraia para uma pasta local

### Passo 2: Criar Ambiente Virtual

Abra o PowerShell como Administrador e navegue até a pasta do projeto:
```powershell
cd C:\caminho\para\projeto
```

Execute o script de setup incluído:
```powershell
.\setup.ps1
```

Este script irá automaticamente:
- ✅ Criar um ambiente virtual em `venv/`
- ✅ Ativar o ambiente virtual
- ✅ Instalar o framework TIR versão 2.4.3
- ✅ Instalar dependências adicionais (pytest, selenium, etc.)

### Passo 3: Configurar o Ambiente no VSCode

1. Abra o projeto no VSCode
2. Pressione `Ctrl+Shift+P` e digite "Python: Select Interpreter"
3. Escolha o interpretador: `./venv/Scripts/python.exe`

### Passo 4: Configurar o TIR

Copie o arquivo template para criar sua configuração:
```powershell
Copy-Item config.template.json config.json
```

Edite o `config.json` com suas configurações específicas (veja [Configuração](#configuração) abaixo).

## 📁 Estrutura do Projeto

```
projeto-tir\
├── venv\                    # Ambiente virtual Python
├── tests\                   # Arquivos de teste automatizados
│   ├── test_basico.py      # Teste básico de exemplo
│   ├── test_crud.py        # Teste CRUD com operações em grid
│   ├── test_formulario.py  # Teste de formulários dinâmicos
│   └── ...                 # Outros testes
├── config.json             # Configuração TIR (personalizada)
├── config.template.json    # Template de configuração
├── setup.ps1               # Script de instalação automatizada
├── .vscode\                # Configurações do VSCode
│   └── settings.json       # Configuração do interpretador Python
├── Log\                    # Logs de execução dos testes
├── screenshot\             # Capturas de tela dos testes
└── README.md               # Este arquivo de documentação
```

## ▶️ Executando Testes

### Ativar Ambiente Virtual
Antes de executar qualquer teste, ative o ambiente virtual:
```powershell
.\venv\Scripts\Activate.ps1
```

### Executar Teste Específico
```powershell
python -m pytest tests/test_basico.py -v
```

### Executar Todos os Testes
```powershell
python -m pytest tests/ -v
```

### Executar Teste Individual (sem pytest)
```powershell
python tests/test_crud.py
```

### Com Relatórios Detalhados
```powershell
python -m pytest tests/ -v --tb=short --html=report.html
```

## ⚙️ Configuração

O arquivo `config.json` contém todas as configurações necessárias para o TIR. Baseie-se no `config.template.json` e personalize conforme seu ambiente.

### Exemplo de Configuração Completa

```json
{
  "Url": "https://ambiente-teste.com.br/webapp/",
  "Browser": "Firefox",
  "Environment": "TESTE",
  "User": "usuario_teste",
  "Password": "sua_senha_aqui",
  "Language": "pt-br",
  "TimeOut": 120,
  "DebugLog": true,
  "Headless": false,
  "POUILogin": true,
  "ChromeDriverAutoInstall": true,
  "LogFolder": "Log/"
}
```

### Parâmetros Importantes

| Parâmetro | Descrição | Valor Padrão |
|-----------|-----------|--------------|
| `Url` | URL do ambiente Protheus Webapp | - |
| `Browser` | Navegador (Firefox, Chrome) | Firefox |
| `Environment` | Ambiente Protheus | - |
| `User` | Usuário para login | - |
| `Password` | Senha do usuário | - |
| `TimeOut` | Timeout em segundos | 120 |
| `DebugLog` | Habilitar logs detalhados | true |
| `Headless` | Executar navegador em modo headless | false |

## 📊 Logs e Debug

### Localização dos Logs
- **Pasta principal**: `Log/`
- **Arquivos**: `TIR_YYYYMMDDHHMMSS.log`
- **Debug habilitado**: Configure `DebugLog: true` no `config.json`

### Dicas de Debug
1. Verifique os logs do TIR em `Log/`
2. Habilite `DebugLog: true` para mais detalhes
3. Verifique os logs do navegador (F12 > Console)
4. Use screenshots em `screenshot/` para análise visual

## 🛠️ Comandos Úteis

### Gerenciamento do Ambiente Virtual
```powershell
# Ativar ambiente
.\venv\Scripts\Activate.ps1

# Desativar ambiente
deactivate

# Remover e recriar ambiente
Remove-Item venv -Recurse -Force
.\setup.ps1
```

### Atualização do TIR
```powershell
.\venv\Scripts\Activate.ps1
pip install --upgrade tir_framework==2.4.3
```

### Verificação da Instalação
```powershell
.\venv\Scripts\Activate.ps1
python -c "import tir; print('TIR instalado com sucesso')"
python -c "import selenium; print('Selenium OK')"
```

### Limpeza de Cache
```powershell
# Limpar cache do Python
.\venv\Scripts\Activate.ps1
python -m pip cache purge

# Limpar logs antigos
Remove-Item Log\*.log -Force
```

## 🔍 Troubleshooting

### Problema: "python não é reconhecido"
**Solução**:
- Certifique-se que Python foi adicionado ao PATH durante a instalação
- Use `py` em vez de `python`:
  ```powershell
  py --version
  ```

### Problema: Erro ao instalar TIR
**Possíveis soluções**:
- Verifique conexão com internet
- Execute PowerShell como Administrador
- Instale manualmente:
  ```powershell
  .\venv\Scripts\Activate.ps1
  pip install tir_framework==2.4.3
  ```

### Problema: Testes falham com timeout
**Soluções**:
- Aumente o `TimeOut` no `config.json` (ex: 300)
- Verifique se o ambiente Protheus está acessível
- Confirme credenciais corretas no `config.json`

### Problema: Grid não avança nas células
**Este é um problema conhecido do TIR**:
- Verifique se o DOM da página mudou (atualizações do sistema)
- Consulte logs em `Log/` para detalhes
- Pode requerer ajustes no código do TIR

### Problema: Erro de WebDriver
**Solução**:
- Configure `ChromeDriverAutoInstall: true` no `config.json`
- Ou baixe manualmente o chromedriver compatível

## 🛠️ Tecnologias Utilizadas

- **Python 3.12**: Linguagem de programação principal
- **TIR Framework**: Framework de automação para Protheus
- **Selenium WebDriver**: Base para automação web
- **Pytest**: Framework de testes
- **Firefox/Chrome**: Navegadores para execução dos testes
- **PowerShell**: Scripts de automação do ambiente
- **VSCode**: Ambiente de desenvolvimento

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

**Projeto pessoal desenvolvido para demonstrar habilidades em automação de testes com TIR Framework** 🚀