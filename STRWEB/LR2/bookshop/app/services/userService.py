from app.repositories.userRepository import UserRepository
from app.core.security import hash_password


class UserService:
    @staticmethod
    def get_by_email(email: str):
        return UserRepository.get_by_email(email)

    @staticmethod
    def update(old_email: str, name: str, phone: str, email: str, password: str):
        return UserRepository.update(old_email, name, phone, email, hash_password(password))

    @staticmethod
    def get_reviews():
        return UserRepository.get_reviews()

    @staticmethod
    def get_review_by_id(id: int):
        return UserRepository.get_review_by_id(id)

    @staticmethod
    def create_review(email: str, rate: int, text: str):
        return UserRepository.create_review(email, rate, text)

    @staticmethod
    def update_review(id: int, rate: int, text: str):
        return UserRepository.update_review(id, rate, text)

    @staticmethod
    def delete_review(id: int):
        return UserRepository.delete_review(id)
