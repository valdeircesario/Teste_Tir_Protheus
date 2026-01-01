# Script PowerShell para criar virtualenv e instalar tir_framework
# Execute no PowerShell com permissões normais em C:\TIR_TESTE

Write-Host "1) Verificando python..."
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    Write-Host "Comando 'python' não encontrado no PATH. Verifique se o Python 3.12 está instalado e no PATH." -ForegroundColor Red
    exit 1
}

Write-Host "Versão do Python:"; python --version

Write-Host "2) Instalando/atualizando pip e virtualenv (no Python global)..."
python -m pip install --upgrade pip virtualenv

Write-Host "3) Criando virtualenv ./venv..."
python -m virtualenv venv

if (-not (Test-Path .\venv\Scripts\python.exe)) {
    Write-Host "Erro: venv não foi criado corretamente ou o caminho esperado não existe." -ForegroundColor Red
    exit 1
}

Write-Host "4) Instalando tir_framework no venv (pode demorar)"
& .\venv\Scripts\python.exe -m pip install tir_framework --no-cache-dir --force-reinstall --upgrade

Write-Host "Setup concluído. Ative o venv com: .\venv\Scripts\Activate.ps1" -ForegroundColor Green
Write-Host "No VSCode, selecione o interpretador: ./venv/Scripts/python.exe"
