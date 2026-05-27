# Gerenciamento de usuarios

# Rotas acessiveis apenas por administradores

from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.usuario import Usuario
from app.auth import get_admin, hash_senha

router = APIRouter(prefix="/usuarios", tags=["Usuario"])

templates = Jinja2Templates(directory="app/templates")

# Listagem dos usuarios
@router.get("/")
def listar_usuarios(
    request: Request,
    db: Session = Depends(get_db),
    admin = Depends(get_admin) # Bloqueia quem não é admin
):
    # Buscar todo os usuarios no banco de dados
    usuarios = db.query(Usuario).order_by(Usuario.nome).all()
    return templates.TemplateResponse(
        request,
        "usuarios/index.html",
        {
            "request": request, 
            "usuarios": usuarios, # Lista para exibir na tela
            "admin": admin # Dados de quem esta logado.
        }
    )