from app.repositories.employeeRepository import EmployeeRepository
from app.core.security import hash_password


class EmployeeService:
    @staticmethod
    def get_all():
        return EmployeeRepository.get_all()

    @staticmethod
    def get_info():
        return EmployeeRepository.get_info()

    @staticmethod
    def get_by_id(id: int):
        return EmployeeRepository.get_by_id(id)

    @staticmethod
    def get_by_email(email: str):
        return EmployeeRepository.get_by_email(email)

    @staticmethod
    def update(old_email: str, name: str, phone: str, email: str, password: str):
        return EmployeeRepository.update(old_email, name, phone, email, hash_password(password))

    @staticmethod
    def add_info(id: int, img, description: str):
        return EmployeeRepository.add_info(id, img, description)

    @staticmethod
    def update_info(id: int, img, description: str):
        return EmployeeRepository.update_info(id, img, description)
