from app.app_models.customerModel import Customer, CustomerReview


class UserRepository:
    @staticmethod
    def get_by_email(email: str):
        try:
            return Customer.objects.filter(email=email).first()
        except:
            return None

    @staticmethod
    def update(old_email: str, name: str, phone: str, email: str, password: str):
        try:
            db_user = UserRepository.get_by_email(old_email)
            if db_user is None:
                return None
            ex_user = Customer.objects.filter(phone=phone).first()
            if ex_user is not None and ex_user.id != db_user.id:
                return 'Phone number already registered!'
            ex_user = Customer.objects.filter(email=email).first()
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
    def get_reviews():
        try:
            return CustomerReview.objects.all()
        except:
            return None

    @staticmethod
    def get_review_by_id(id: int):
        try:
            return CustomerReview.objects.filter(id=id).first()
        except:
            return None

    @staticmethod
    def create_review(email: str, rate: int, text: str):
        try:
            user = UserRepository.get_by_email(email)
            if user is None:
                return None
            review = CustomerReview.objects.create(
                user=user, rate=rate, text=text)
            review.save()
            return review
        except:
            return None

    @staticmethod
    def update_review(id: int, rate: int, text: str):
        try:
            review = CustomerReview.objects.filter(id=id).first()
            if review is None:
                return None
            review.rate = rate
            review.text = text
            review.save()
            return review
        except:
            return None

    @staticmethod
    def delete_review(id: int):
        try:
            review = CustomerReview.objects.filter(id=id).first()
            if review is None:
                return None
            review.delete()
            return 'ok'
        except:
            return None
