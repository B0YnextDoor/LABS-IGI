from app.app_models.employeeModels import Employee, EmployeeInfo


class EmployeeRepository:
    @staticmethod
    def get_all():
        try:
            return Employee.objects.all()
        except:
            return None

    @staticmethod
    def get_by_ids(ids: list[str]):
        empls = list()
        for id in ids:
            empl = EmployeeRepository.get_by_id(int(id))
            if empl is not None:
                empls.append(
                    {'name': empl.name, 'post': empl.employeeinfo.description})
        return empls

    @ staticmethod
    def get_by_id(id: int):
        try:
            return Employee.objects.filter(id=id).first()
        except:
            return None

    @ staticmethod
    def get_by_email(email: str):
        try:
            return Employee.objects.filter(email=email).first()
        except:
            None

    @ staticmethod
    def create(name: str, phone: str, email: str, password: str):
        try:
            ex_user = Employee.objects.filter(email=email).first()
            if ex_user is not None:
                return 'Email already registered!'
            ex_user = Employee.objects.filter(phone=phone).first()
            if ex_user is not None:
                return 'Phone number already registered!'
            new_emp = Employee.objects.create(name=name, phone=phone,
                                              email=email, password=password, is_admin=False)
            new_emp.save()
            return new_emp
        except:
            return None

    @ staticmethod
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

    @ staticmethod
    def get_info(sort_by: str):
        try:
            empls = Employee.objects.filter(is_admin=False)
            idx = sort_by.find("description")
            if (idx != -1):
                dir = "" if idx == 0 else '-'
                empls = empls.select_related('employeeinfo').order_by(
                    f'{dir}employeeinfo__description')
            else:
                empls = empls.order_by(f"{sort_by}")
            return empls
        except Exception as e:
            print(e)
            return None

    @ staticmethod
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
            if img is not None:
                db_user.employeeinfo.img = img
            db_user.employeeinfo.description = description
            db_user.employeeinfo.save()
            db_user.save()
            return db_user
        except:
            return None
