import requests
import json
import random
import time
from settings import Settings


class AstrologBot():
    """Класс бота

    Принимает запросы на гороскоп, ищет гороскоп в базе гороскопов
    и отправляет  его пользователю
    """

    def __init__(self):
        """Метод инициализации класса AstrologBot

        Готовит API и загружает словарь гороскопа.
        """
        self.settings = Settings()
        self.url = self.settings.url + self.settings.token + '/'

        with open('updates_id.txt', 'r') as self.updates_file:
            self.last_update_id = int(self.updates_file.read())

        # Чтение файла гороскопов и передача словаря гороскопов в переменную
        with open('astrological_predictions.json', 'r') as self.file:
            self.predictions = json.load(self.file)

    def get_updates(self):
        """Метод запрашивает обновление у сервера Telegram"""

        get_updates_url = self.url + 'getupdates'
        self.request = requests.get(get_updates_url)
        return self.request.json()

    def get_random_prediction(self, list_prediction):
        """Метод случайно выбирает гороскоп из списка"""
        return random.choice(list_prediction)

    def request_processing(self):
        """Метод обрабатывает входящие запросы"""
        self.data = self.get_updates()

        # Проверяем наличие новых сообщений.
        for index in range(len(self.data["result"])):
            self.last_request = self.data["result"][index]
            self.update_id = self.last_request["update_id"]
            if self.update_id > self.last_update_id:
                self.chat_id = self.last_request["message"]["chat"]["id"]
                self.message_text = self.last_request["message"]["text"]
                self.my_ansver = self.message_processing(self.message_text)
                self.send_ansver(self.chat_id, self.my_ansver)
                self.last_update_id = self.update_id
                with open('updates_id.txt', 'w') as self.updates_file:
                    self.updates_file.write(str(self.update_id))

    def message_processing(self, message: str):
        """Метод обрабатывает сообщения от пользователей"""
        if message == "/today":
            return self.get_random_prediction(self.predictions["daily"])
        elif message == "/tommorow":
            return self.get_random_prediction(self.predictions["daily"])
        elif message == "/week":
            return self.get_random_prediction(self.predictions["weekly"])
        elif message == "/month":
            return self.get_random_prediction(self.predictions["monthly"])
        elif message == "/help":
            return self.predictions["help"]
        else:
            return "Введите /help"

    def send_ansver(self, chat_id: int, ansver: str):
        send_url = self.url + 'sendmessage?chat_id={}&text={}'.format(
            chat_id, ansver)
        requests.get(send_url)


def main():
    """Метод выполнения модуля"""
    astrolog = AstrologBot()
    while True:
        astrolog.get_updates()
        astrolog.request_processing()


if __name__ == '__main__':
        main()
