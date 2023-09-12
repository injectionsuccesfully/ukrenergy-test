from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from configs.config import get_settings

engine = create_engine(
    get_settings().sqlalchemy_database_url,
    echo=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db_session():
    db = SessionLocal()
    try:
        print('Open db connection: ')
        yield db
    finally:
        print('Close db connection: ')
        db.close()

def create_database_structure():
    Base.metadata.create_all(bind=engine)