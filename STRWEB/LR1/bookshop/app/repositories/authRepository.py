from app.app_models.customerModel import Customer
from app.app_models.employeeModels import Employee


class AuthRepository:
    @staticmethod
    def sign_up(name: str, phone: str, email: str, password: str):
        try:
            db_user = Customer.objects.filter(phone=phone).first()
            if db_user is not None:
                return 'Phone number already registered!'
            db_user = Customer.objects.filter(email=email).first()
            if db_user is not None:
                return 'Email already registered!'
            new_customer = Customer(name=name, phone=phone, email=email,
                                    password=password)
            new_customer.save()
            new_customer.refresh_from_db()
            return new_customer
        except:
            return None

    @staticmethod
    def sign_in(email: str):
        role = 'usr'
        user = Customer.objects.filter(email=email).first()
        if user is None:
            user = Employee.objects.filter(email=email).first()
            role = 'emp'
        return (user, role)
