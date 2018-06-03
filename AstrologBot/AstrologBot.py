import requests
import json
import ssl_fix
from settings import Settings


class AstrologBot():
    """Класс бота

    Принимает запросы на гороскоп, ищет гороскоп в базе гороскопов
    и отправляет  его пользователю
    """

    def __init__(self):
        self.settings = Settings()
        self.url = self.settings.url + self.settings.token + '/'

    def get_updates(self, url):
        """Метод запрашивает обновление у сервера Telegram"""

        get_updates_url = url + 'getupdates'
        r = requests.get(get_updates_url)
        print(r.json())


def main():
    """Метод выполнения модуля"""
    astrolog = AstrologBot()
    astrolog.get_updates(astrolog.url)


if __name__ == '__main__':
    main()
