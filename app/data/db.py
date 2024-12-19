import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import DATABASE_URL
from app.data.models import Base

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

print("Database URL from config:", DATABASE_URL)
print("Database engine created successfully")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, 'test.db')

print(f"Абсолютный путь к базе данных: {DB_PATH}")

if os.path.exists(DB_PATH):
    print("✅ Файл базы данных существует")
else:
    print("❌ Файл базы данных НЕ существует")

print("Создаём таблицы...")
Base.metadata.create_all(bind=engine)
print("✅ Таблицы успешно созданы")