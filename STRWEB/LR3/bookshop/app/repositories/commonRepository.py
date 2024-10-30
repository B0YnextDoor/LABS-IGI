from app.app_models import commonModels as cm


class InfoRepository:
    @staticmethod
    def get():
        try:
            if cm.AboutInfo.objects.first() is None:
                cm.AboutInfo().save()
            return cm.AboutInfo.objects.first()
        except:
            return None

    @staticmethod
    def update(info, logo, video, history, requisites, certificate):
        try:
            db_info = cm.AboutInfo.objects.first()
            if db_info is None:
                return None
            db_info.info = info
            if logo is not None:
                db_info.logo = logo
            if video is not None:
                db_info.video = video
            db_info.history = history
            db_info.requisites = requisites
            db_info.certificate = certificate
            db_info.save()
            return db_info
        except Exception as e:
            print(e)
            return None


class NewsRepository:
    @staticmethod
    def reform_text(text):
        if text[-1] not in ['.', '?', '!']:
            text += '.'
        return text

    @staticmethod
    def get_all():
        try:
            return cm.News.objects.all()
        except:
            return None

    @staticmethod
    def get_by_id(id: int):
        try:
            return cm.News.objects.filter(id=id).first()
        except:
            return None

    @staticmethod
    def create(title: str, text: str, img):
        try:
            news = cm.News.objects.create(
                title=title, text=NewsRepository.reform_text(text), img=img)
            news.save()
            return news
        except:
            return None

    @staticmethod
    def update(id: int, title: str, text: str, img):
        try:
            news = cm.News.objects.filter(id=id).first()
            if news is None:
                return None
            news.title = title
            news.text = NewsRepository.reform_text(text)
            if img is not None:
                news.img = img
            news.save()
            return news
        except:
            return None

    @staticmethod
    def delete(id: int):
        try:
            news = cm.News.objects.filter(id=id).first()
            if news is None:
                return None
            news.delete()
            return 'ok'
        except:
            return None


class QARepository:
    @staticmethod
    def get_all():
        try:
            return cm.QA.objects.all()
        except:
            return None

    @staticmethod
    def get_by_id(id: int):
        try:
            return cm.QA.objects.filter(id=id).first()
        except:
            return None

    @staticmethod
    def create(question: str, answer: str):
        try:
            qa = cm.QA.objects.create(question=question, answer=answer)
            qa.save()
            return qa
        except:
            return None

    @staticmethod
    def update(id: int, question: str, answer: str):
        try:
            qa = cm.QA.objects.filter(id=id).first()
            if qa is None:
                return None
            qa.question = question
            qa.answer = answer
            qa.save()
            return qa
        except:
            return None

    @staticmethod
    def delete(id: int):
        try:
            qa = cm.QA.objects.filter(id=id).first()
            if qa is None:
                return None
            qa.delete()
            return 'ok'
        except:
            return None


class VacancyRepository:
    @staticmethod
    def get_all():
        try:
            return cm.Vacancy.objects.all()
        except:
            return None

    @staticmethod
    def get_by_id(id: int):
        try:
            return cm.Vacancy.objects.filter(id=id).first()
        except:
            return None

    @staticmethod
    def create(name: str, description: str):
        try:
            vacancy = cm.Vacancy.objects.create(
                name=name, description=description)
            vacancy.save()
            return vacancy
        except:
            return None

    @staticmethod
    def update(id: int, name: str, description: str):
        try:
            db_vac = VacancyRepository.get_by_id(id)
            if db_vac is None:
                return None
            db_vac.name = name
            db_vac.description = description
            db_vac.save()
            return db_vac
        except:
            return None

    @staticmethod
    def delete(id: int):
        try:
            db_vac = VacancyRepository.get_by_id(id)
            if db_vac is None:
                return None
            db_vac.delete()
            return 'ok'
        except:
            return None


class PartnerRepository:
    @staticmethod
    def get_all():
        try:
            return cm.CompanyPartner.objects.all()
        except:
            return None


class BannerRepository:
    @staticmethod
    def get():
        try:
            return cm.BannerSettings.objects.first()
        except:
            return None

    @staticmethod
    def update(loop: bool, navs: bool, pags: bool, auto: bool, stopMouseHover: bool, delay: float):
        try:
            settings = cm.BannerSettings.objects.first()
            if settings is None:
                return None
            settings.loop = loop
            settings.navs = navs
            settings.pags = pags
            settings.auto = auto
            settings.stopMouseHover = stopMouseHover
            settings.delay = delay
            settings.save()
            return True
        except:
            return None
