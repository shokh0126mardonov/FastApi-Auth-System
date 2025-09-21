from dotenv import load_dotenv
import os
from fastapi_mail import ConnectionConfig

load_dotenv()

class Settings:

    #Database config
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_HOST = os.getenv("DB_HOST")
    DB_PASSWORD = os.getenv("DB_PASSWORD")

    #mail config
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_FROM = os.getenv("MAIL_FROM")
    MAIL_PORT = int(os.getenv("MAIL_PORT"))
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    
settings = Settings()

mail_conf = ConnectionConfig(
    MAIL_USERNAME = Settings.MAIL_USERNAME,
    MAIL_PASSWORD = Settings.MAIL_PASSWORD,
    MAIL_FROM = Settings.MAIL_FROM,
    MAIL_PORT = Settings.MAIL_PORT,
    MAIL_SERVER = Settings.MAIL_SERVER,
    MAIL_STARTTLS=True,   
    MAIL_SSL_TLS=False, 
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)