import requests
import json
import random
from settings import Settings


class AstrologBot():
    """Класс бота

    Принимает запросы на гороскоп, ищет гороскоп в базе гороскопов
    и отправляет  его пользователю
    """

    def __init__(self):
        """Метод инициализации класса AstrologBot

        Готовит AP и загружает словарь гороскопа.
        """
        self.settings = Settings()
        self.url = self.settings.url + self.settings.token + '/'

        # Читение файла гороскопов и передача словаря гороскопов в переменную
        with open('astrological_predictions.json', 'r',
                    encoding='utf-8') as self.file:
            self.predictions = json.load(self.file)

    def get_updates(self, url):
        """Метод запрашивает обновление у сервера Telegram"""

        get_updates_url = url + 'getupdates'
        self.request = requests.get(get_updates_url)
        print(self.request.json())

    def get_random_prediction(self, list_prediction):
        """Метод случайно выбирает гороскоп из списка

        в max_lenght передается длинна списка.
        """
        return random.choice(list_prediction)


def main():
    """Метод выполнения модуля"""
    astrolog = AstrologBot()
    # astrolog.get_updates(astrolog.url)
    print(astrolog.get_random_prediction(astrolog.predictions['daily']))


if __name__ == '__main__':
    main()
