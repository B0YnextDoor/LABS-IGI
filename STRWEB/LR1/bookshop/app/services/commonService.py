from app.repositories.commonRepository import InfoRepository, NewsRepository, \
    QARepository, VacancyRepository, PartnerRepository


class InfoService:
    @staticmethod
    def get():
        info = InfoRepository.get()
        return {'info': info.info, 'logo': info.logo, 'video': info.video,
                'history': info.history, 'requisites': info.requisites, 'certificate': info.certificate}

    @staticmethod
    def update(info, logo, video, history, requisites, certificate):
        print(video)
        return InfoRepository.update(info, logo, video, history, requisites, certificate)


class NewsService:
    @staticmethod
    def get_all():
        db_news = NewsRepository.get_all().reverse()
        return [{'id': news.id, 'title': news.title, 'text': news.text.split('.')[0], 'img': news.img,
                 'method': news.get_absolute_url} for news in db_news]

    @staticmethod
    def get_by_id(id: int):
        return NewsRepository.get_by_id(id)

    @staticmethod
    def create(title: str, text: str, img):
        return NewsRepository.create(title, text, img)

    @staticmethod
    def update(id: int, title: str, text: str, img):
        return NewsRepository.update(id, title, text, img)

    @staticmethod
    def delete(id: int):
        return NewsRepository.delete(id)


class QAService:
    @staticmethod
    def get_all():
        return QARepository.get_all()

    @staticmethod
    def get_by_id(id: int):
        return QARepository.get_by_id(id)

    @staticmethod
    def create(question: str, answer: str):
        return QARepository.create(question, answer)

    @staticmethod
    def update(id: int, question: str, answer: str):
        return QARepository.update(id, question, answer)

    @staticmethod
    def delete(id: int):
        return QARepository.delete(id)


class VacancyService:
    @staticmethod
    def get_all():
        return VacancyRepository.get_all()

    @staticmethod
    def get_by_id(id: int):
        return VacancyRepository.get_by_id(id)

    @staticmethod
    def create(name: str, description: str):
        return VacancyRepository.create(name, description)

    @staticmethod
    def update(id: int, name: str, description: str):
        return VacancyRepository.update(id, name, description)

    @staticmethod
    def delete(id: int):
        return VacancyRepository.delete(id)


class PartnerService:
    @staticmethod
    def get_all():
        return PartnerRepository.get_all()
