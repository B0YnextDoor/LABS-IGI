from app.app_models.commonModels import SaleCode


class SaleRepository:
    @staticmethod
    def reform(db_codes):
        codes = list()
        for id, code in enumerate(db_codes):
            sale = code.code.split('_')
            codes.append(
                {'id': code.id, 'order': id + 1, 'code': code.code, 'is_active': code.is_active, 'sale': int(sale[1])})
        return codes

    @staticmethod
    def get_all():
        try:
            return SaleRepository.reform(SaleCode.objects.all())
        except:
            return None

    @staticmethod
    def get_active():
        try:
            return SaleRepository.reform(SaleCode.objects.filter(is_active=True))
        except:
            return None

    @staticmethod
    def check_code(code: str):
        try:
            return SaleCode.objects.filter(
                is_active=True, code=code).first() is not None
        except:
            return False

    @staticmethod
    def create(code: str, is_active: bool):
        try:
            new_code = SaleCode.objects.create(code=code, is_active=is_active)
            new_code.save()
            return new_code
        except:
            return None

    @staticmethod
    def update(id: int):
        try:
            db_code = SaleCode.objects.filter(id=id).first()
            if db_code is None:
                return None
            db_code.is_active = not db_code.is_active
            db_code.save()
            return db_code
        except:
            return None

    @staticmethod
    def delete(id: int):
        try:
            db_code = SaleCode.objects.filter(id=id).first()
            if db_code is None:
                return None
            db_code.delete()
            return 'ok'
        except:
            return None
