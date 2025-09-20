from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker

from .config import settings

url_object = URL.create(
    drivername="postgresql+psycopg2",
    username=settings.DB_USER,
    port=settings.DB_PORT,
    password=settings.DB_PASSWORD,
    host=settings.DB_HOST,
    database=settings.DB_NAME
)

engine = create_engine(url_object)

Base = declarative_base()

Localsession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = Localsession()
    try:
        yield db
    finally:
        db.close()
