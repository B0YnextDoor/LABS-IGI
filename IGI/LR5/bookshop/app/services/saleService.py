from app.repositories.saleRepository import SaleRepository


class SaleService:
    @staticmethod
    def get_all():
        return SaleRepository.get_all()

    @staticmethod
    def get_active():
        return SaleRepository.get_active()

    @staticmethod
    def check_code(code: str):
        return SaleRepository.check_code(code)

    @staticmethod
    def create(code: str, is_active: bool):
        return SaleRepository.create(code, is_active)

    @staticmethod
    def update(id: int):
        return SaleRepository.update(id)

    @staticmethod
    def delete(id: int):
        return SaleRepository.delete(id)
