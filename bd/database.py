from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
import bcrypt

# URL de conexão com MySQL sem o nome do banco de dados
DATABASE_URL = "mysql+pymysql://root:root@127.0.0.1:3306/"

# Criar a conexão ao MySQL
engine = create_engine(DATABASE_URL)

# Tentar criar o banco de dados Login, caso não exista
try:
    with engine.connect() as conn:
        conn.execute("CREATE DATABASE IF NOT EXISTS Login")
        print("Banco de dados 'Login' criado ou já existe.")
except OperationalError as e:
    print(f"Erro ao criar o banco de dados: {e}")

# Alterar a URL para incluir o nome do banco 'Login'
DATABASE_URL = "mysql+pymysql://root:root@127.0.0.1:3306/Login"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modelo do Usuário
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50), unique=True, nullable=False)
    senha_hash = Column(String(255), nullable=False)

# Criar as tabelas no banco de dados 'Login'
Base.metadata.create_all(bind=engine)

# Funções CRUD
def criar_usuario(nome: str, senha: str):
    session = SessionLocal()
    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
    usuario = Usuario(nome=nome, senha_hash=senha_hash.decode('utf-8'))
    session.add(usuario)
    session.commit()
    session.close()

def autenticar_usuario(nome: str, senha: str):
    session = SessionLocal()
    usuario = session.query(Usuario).filter_by(nome=nome).first()
    session.close()
    if usuario and bcrypt.checkpw(senha.encode('utf-8'), usuario.senha_hash.encode('utf-8')):
        return True
    return False

# Função para verificar se o nome de usuário já existe
def usuario_existe(nome: str):
    session = SessionLocal()
    usuario = session.query(Usuario).filter_by(nome=nome).first()
    session.close()
    return usuario is not None
