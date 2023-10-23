import requests


class HeadHunterAPI():
    """
    Класс для работы с API сайта www.headhunter.ru
    """

    def __init__(self):
        """
        Создание экземпляра класса сайта https://api.hh.ru/vacancies
        """
        self.url_address = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, employer_id) -> dict:
        """
        Функция для получения данных сайта от выбранной компании

        :return данные в формате словаря
        """
        response = requests.get(self.url_address, params={'per_page': 100, 'employer_id': employer_id,
                                'only_with_salary': True, 'period': 7})
        vacancies_dict = response.json()
        return vacancies_dict['items']
