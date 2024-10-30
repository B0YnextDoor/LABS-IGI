from app.repositories.employeeRepository import EmployeeRepository
from app.core.security import hash_password
import re


def normalize_phone_number(phone):
    digits = re.sub(r'\D', '', phone)
    if digits.startswith('375'):
        digits = digits[3:]
    elif digits.startswith('80'):
        digits = digits[2:]

    return f"+375{digits}"


limit = 3


class EmployeeService:
    @staticmethod
    def get_all():
        return EmployeeRepository.get_all()

    @staticmethod
    def get_by_ids(ids: list[str]):
        result = dict()
        result['data'] = EmployeeRepository.get_by_ids(ids)
        return result

    @staticmethod
    def filter_employees(employees, search_string: str):
        search_string = search_string.lower()
        return [
            employee for employee in employees
            if any(search_string in str(value).lower() for value in employee.values())
        ]

    @staticmethod
    def get_info(page: int, sort_by: str | None, filter: str | None):
        fields = ['name', 'email', 'phone', 'description']
        if (sort_by is None or (sort_by not in fields and sort_by[1:] not in fields)):
            sort_by = 'name'
        if filter is None:
            filter = ""
        offset = page*limit
        empls = EmployeeRepository.get_info(sort_by)
        if empls is None:
            return {"error": "server error"}
        result = dict()
        contacts = list()
        for emp in empls:
            contacts.append({
                "id": emp.id,
                "name": emp.name,
                "email": emp.email,
                "phone": emp.phone,
                "img": emp.employeeinfo.img.url,
                "description": emp.employeeinfo.description
            })
        if len(filter) > 0:
            contacts = EmployeeService.filter_employees(contacts, filter)
        result['total'] = len(contacts)
        result['contacts'] = contacts[offset:offset + limit]
        return result

    @staticmethod
    def get_by_id(id: int):
        return EmployeeRepository.get_by_id(id)

    @staticmethod
    def get_by_email(email: str):
        return EmployeeRepository.get_by_email(email)

    @staticmethod
    def create(name: str, phone: str, email: str):
        return EmployeeRepository.create(name, normalize_phone_number(phone), email, hash_password("Test123test"))

    @staticmethod
    def update(old_email: str, name: str, phone: str, email: str, password: str):
        return EmployeeRepository.update(old_email, name, phone, email, hash_password(password))

    @staticmethod
    def add_info(id: int, img, description: str):
        return EmployeeRepository.add_info(id, img, description)

    @staticmethod
    def update_info(id: int, img, description: str):
        return EmployeeRepository.update_info(id, img, description)
