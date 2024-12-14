from app.repository.user_repository import UserRepository
from app.domain.user import User

class UserService:
    def __init__(self, db):
        self.user_repository = UserRepository(db)

    def create_user(self, username: str, email: str) -> User:
        user_model = self.user_repository.create_user(username, email)
        return User(username=user_model.username, email=user_model.email)

    def get_user(self, user_id: int) -> User:
        user_model = self.user_repository.get_user(user_id)
        if user_model:
            return User(username=user_model.username, email=user_model.email)
        return None

    def get_all_users(self):
        users = self.user_repository.get_all_users()
        return [User(username=user.username, email=user.email) for user in users]
