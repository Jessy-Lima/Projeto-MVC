# Instalar as bibliotecas

no terminal:
```bash
pip install -r requirements.txt
```

# Inicializar o alembic
no terminal:
```bash
python -m alembic init migrations
```
# Editar o arquivo alembic init - na linha 89:
sqlealchemy.url = 

# Gerar a migrations
no terminal:
```bash
python -m alembic revision --autogenerate -m "Criar tabela usuarios"
```

# Aplicar a migrations no banco
```bash
python -m alembic upgrade head
```