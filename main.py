from src.class_api import HeadHunterAPI
from src.class_DB import DBManager
from src.utils import load_employers


def main():
    # загружаем данные компаний
    employers_dict = load_employers('src/employers_id.json')

    # создаем экземпляры для работы с API и БД
    hh_api = HeadHunterAPI()
    hh_manager_db = DBManager()

    # создаем необходимые таблицы
    hh_manager_db.create_table_employers()
    hh_manager_db.create_table_vacancies()

    # заполняем таблицу данными интересующих компаний
    for employer in employers_dict:
        hh_manager_db.insert_table_employers(employer)
    # заполняем таблицу данными по вакансиям от указанных компаний
    for employer in employers_dict:
        employers_vacancies = hh_api.get_vacancies(employer['id'])
        for vacancies_info in employers_vacancies:
            hh_manager_db.insert_table_vacancies(vacancies_info)


if __name__ == '__main__':
    main()
