from app.app_models.employeeModels import Employee, EmployeeInfo


class EmployeeRepository:
    @staticmethod
    def get_all():
        try:
            return Employee.objects.all()
        except:
            return None

    @staticmethod
    def get_by_id(id: int):
        try:
            return Employee.objects.filter(id=id).first()
        except:
            return None

    @staticmethod
    def get_by_email(email: str):
        try:
            return Employee.objects.filter(email=email).first()
        except:
            None

    @staticmethod
    def update(old_email: str, name: str, phone: str, email: str, password: str):
        try:
            db_user = EmployeeRepository.get_by_email(old_email)
            if db_user is None:
                return None
            ex_user = Employee.objects.filter(phone=phone).first()
            if ex_user is not None and ex_user.id != db_user.id:
                return 'Phone number already registered!'
            ex_user = Employee.objects.filter(email=email).first()
            if ex_user is not None and ex_user.id != db_user.id:
                return 'Email already registered!'
            db_user.name = name
            db_user.phone = phone
            db_user.email = email
            db_user.password = password
            db_user.save()
            return db_user
        except:
            return None

    @staticmethod
    def get_info():
        try:
            empls = filter(lambda e: e.is_admin == False,
                           EmployeeRepository.get_all())
            has_info = list()
            no_info = list()
            for empl in empls:
                info = EmployeeInfo.objects.filter(employee_id=empl).first()
                if info is None:
                    no_info.append(empl)
                else:
                    has_info.append(empl)
            return has_info, no_info
        except:
            return None, None

    @staticmethod
    def add_info(id: int, img, description: str):
        try:
            db_user = EmployeeRepository.get_by_id(id)
            if db_user is None:
                return None
            info = EmployeeInfo.objects.create(
                employee_id=db_user, img=img, description=description)
            info.save()
            db_user.save()
            return info
        except:
            return None

    @staticmethod
    def update_info(id: int, img, description: str):
        try:
            db_user = EmployeeRepository.get_by_id(id)
            if db_user is None:
                return None
            db_user.employeeinfo.img = img
            db_user.employeeinfo.description = description
            db_user.employeeinfo.save()
            db_user.save()
            return db_user
        except:
            return None
