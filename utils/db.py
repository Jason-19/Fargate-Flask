"""
secret manager 
La rotación automática y la centralización de credenciales reducen la probabilidad de errores operativos.
Se cobra por número de secretos almacenados y solicitudes de recuperación,
"""
from http.client import HTTPException
import json
import boto3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging
log = logging.getLogger(__name__)

def getSecretManagerDB():
    secret_name = "MySecretForAppGamerVault"  
    region_name = "us-east-1"   
    
    try:
        client = boto3.client("secretsmanager", region_name=region_name)
        response = client.get_secret_value(SecretId=secret_name)
        secret = json.loads(response["SecretString"])
        return secret
    except Exception as e:
        log.error(f"Error{e}")
        return None
    

# db_credentials = getSecretManagerDB()

# DB_HOST = db_credentials["host"]
# DB_NAME = db_credentials["dbname"]
# DB_USER = db_credentials["username"]
# DB_PASS = db_credentials["password"]

# local databse
DB_HOST = 'localhost'
# DB_HOST = 'database_GamerVault'
DB_NAME = 'gamervaultlts'
DB_USER = 'root'
DB_PASS = 'root'

DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()
Base = declarative_base()

    
def get_db():
    try:
        log.info("Obteniendo sesion de Base de Datos")
        yield db
    except Exception as e:
        log.error(str(e))
        db.close()
        raise HTTPException(status_code=500, detail='ERROR - DATABASE FAIL')
    finally:
        db.close()

def verify_db_connection():
    try:
        with engine.connect() as conn:
            conn.execute("SHOW DATABASES")
        log.info("Conexion exitosa")
        return True
    except Exception as e:
        log.critical(f"No se pudo conectar a la base de datos: {str(e)}")
        return False
    
    
verify_db_connection()