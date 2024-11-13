from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# Definindo parâmetros para acesso
db_user = "aluno"
db_password = "aluno_senha"
db_name = "meu_banco"
db_host = "localhost"
db_port = "3306"

# Endereço (URL) para conexão
DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Criando banco de dados
db = create_engine(DATABASE_URL)

# Criando conexão com banco de dados
Session = sessionmaker(bind=db)
session = Session()

# Gerenciando conexão com banco de dados
@contextmanager
def get_db():
    db = Session()
    try:
        yield db
        # Salvando no DB
        db.commit() 
    except Exception as erro:
        # Caso ocorra algum erro, desfaz alterações no BD 
        db.rollback() 
    finally:
        #Fecha conexão com BD
        db.close() 