#  Script para popular o banco de dados com usuarios admin

from app.database import Session
from app.models.usuario import Usuario
from app.auth import hash_senha

# Função para cadastrar os usuarios
def seed():
    db = Session()
    try:
        nome_usuario = "admin"
        email_usuario = "admin@teste.com"
        senha_usuario = "admin@123"
        perfil = "admin"

        # Verificar se o usuário ja existe
        existente = db.query(Usuario).filter_by(email=email_usuario).first()
        if not existente:
            # Criar o usuário
            usuario =  Usuario(
                nome=nome_usuario,
                email=email_usuario,
                senha_hash=hash_senha(senha_usuario),
                role=perfil
            )
            db.add(usuario)
            db.commit()
            print(f"Usuario cadastrado com sucesso {nome_usuario}")
        else:
            print(f"Esse email ha está cadastrado!")

    except Exception as erro:
        db.rollback()
        print(f"Erro: {erro}")
    finally:
        db.close()

#Chamar a função
seed()