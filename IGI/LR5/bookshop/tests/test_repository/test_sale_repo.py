from django.test import TestCase
from app.app_models.commonModels import SaleCode
from app.repositories.saleRepository import SaleRepository


class SaleRepositoryTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        SaleCode.objects.create(code='TestCode_10', is_active=True)
        SaleCode.objects.create(code='TestCode_20', is_active=False)

    def test_get_all(self):
        codes = SaleRepository.get_all()
        self.assertIsNotNone(codes)
        self.assertEquals(len(codes), 2)
        self.assertEquals(codes[0]['code'], 'TestCode_20')
        self.assertEquals(codes[1]['code'], 'TestCode_10')

    def test_get_active(self):
        codes = SaleRepository.get_active()
        self.assertIsNotNone(codes)
        self.assertEquals(len(codes), 1)
        self.assertEquals(codes[0]['code'], 'TestCode_10')

    def test_check_code(self):
        self.assertTrue(SaleRepository.check_code('TestCode_10'))
        self.assertFalse(SaleRepository.check_code('TestCode'))

    def test_create(self):
        code = SaleRepository.create('TestCode_30', False)
        self.assertIsNotNone(code)
        self.assertFalse(code.is_active)
        self.assertEquals(code.code, 'TestCode_30')

    def test_update(self):
        code = SaleRepository.update(2)
        self.assertIsNotNone(code)
        self.assertTrue(code.is_active)
        self.assertEquals(code.id, 2)

    def test_delete(self):
        code = SaleRepository.delete(1)
        self.assertEquals(code, 'ok')
