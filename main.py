from src.class_api import HeadHunterAPI
from src.class_DB import DBManager
from src.utils import load_employers


def main():
    # загружаем данные компаний
    employers_dict = load_employers('src/employers_id.json')

    # создаем экземпляры для работы с API и БД
    hh_api = HeadHunterAPI()
    hh_manager_db = DBManager()

    # создаем необходимую таблицу
    hh_manager_db.create_table()

    # заполняем таблицу данными необходимых компаний
    for employer in employers_dict:
        employers_vacancies = hh_api.get_vacancies(employer['id'])
        for vacancies_info in employers_vacancies:
            hh_manager_db.insert_table(vacancies_info)


if __name__ == '__main__':
    main()
