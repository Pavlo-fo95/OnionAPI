import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

Base = declarative_base()  # Объявление базового класса для моделей

# Получаем путь к базе данных из переменных окружения
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{os.path.join(os.getcwd(), 'test.db')}")
print("Database path:", DATABASE_URL)

# Создаём подключение
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Убедимся, что папка для базы данных существует
db_folder = os.path.dirname(DATABASE_URL.replace("sqlite:///", ""))
if not os.path.exists(db_folder):
    os.makedirs(db_folder)

# Создаём таблицы
Base.metadata.create_all(bind=engine)
print("Таблицы созданы успешно!")
