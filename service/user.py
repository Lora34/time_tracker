
from dataclasses import dataclass
from random import random, choice
import string
from repository.user import UserRepository
from schema import UserLoginSchema



@dataclass
class UserService:
    user_repository: UserRepository

    def create_user(self, username: str, password: str) -> UserLoginSchema:
        user = self.user_repository.create_user(username, password)
        return UserLoginSchema(user_id=user.id, access_token=user.access_token)
    
    @staticmethod
    def _generate_access_token(self) -> str:
        return ''.join(choice(string.ascii_uppercase + string.digits) for _ in range(10))
    
