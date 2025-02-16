# konfigurasi database
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"

# Membuat engine database untuk berkomunikasi dengan SQLite
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# Membuat sesi database dengan konfigurasi tertentu
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Membuat kelas dasar untuk deklarasi model
Base = declarative_base()