# Segurança: Executar este script na raiz do repositório com Git instalado.
# Ele cria uma branch, adiciona .gitignore e config.json.example e remove do rastreamento arquivos gerados preservando-os localmente.

# 1) Crie branch de trabalho
git checkout -b chore/add-gitignore

# 2) Commit das novas regras
git add .gitignore config.json.example
git commit -m "chore: add .gitignore and config.json.example"

# 3) Desaloca arquivos do controle de versão (mantém localmente)
git rm --cached -r --ignore-unmatch .venv venv __pycache__ Log screenshot report_*.html .pytest_cache pytest_run.log
git rm --cached --ignore-unmatch config.json

# 4) Commit das remoções
git commit -m "chore: untrack generated and sensitive files"

# 5) Dica: testar tudo localmente, rodar os testes e só então push
# git push origin chore/add-gitignore

Write-Host "Script concluído. Revise `git status` e rode os testes localmente." -ForegroundColor Green
