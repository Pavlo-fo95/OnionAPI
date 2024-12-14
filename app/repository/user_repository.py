from sqlalchemy.orm import Session
from app.data.models import UserModel

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, username: str, email: str) -> UserModel:
        user = UserModel(username=username, email=email)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user(self, user_id: int) -> UserModel:
        return self.db.query(UserModel).filter(UserModel.id == user_id).first()

    def get_all_users(self):
        return self.db.query(UserModel).all()
