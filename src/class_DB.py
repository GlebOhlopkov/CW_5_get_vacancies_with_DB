from src.utils import config
import psycopg2


class DBManager():
    """
    Класс для работы с базой данных PostgreSQL (pgAdmin)
    """

    def __init__(self):
        """
        Создание экземпляра класса для работы с базой данных, указанной в database.ini
        """
        self.db_config: dict = config()

    def create_table(self) -> None:
        """
        Функция для создания таблицы с компаниями и вакансиями (и информации по ним)
        :return:
        """
        with psycopg2.connect(**self.db_config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE employers (
                        employer_title VARCHAR,
                        vacancy_id INTEGER,
                        vacancy_name VARCHAR,
                        vacancy_url VARCHAR,
                        vacancy_salary_from INTEGER
                    )
                """)
            conn.commit()

    def insert_table(self, json_info: dict) -> None:
        """
        Функция для заполнения таблицы в базе данных
        :param json_info: информация по компаниям и вакансиям в формате json
        :return:
        """
        with psycopg2.connect(**self.db_config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO employers
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    (json_info['employer']['name'], json_info['id'], json_info['name'],
                     json_info['url'], json_info['salary']['from'])
                )
            conn.commit()

    def get_companies_and_vacancies_count(self) -> None:
        """
        Функция для получения списка всех компаний и количества вакансий у каждой компании.
        :return:
        """
        with psycopg2.connect(**self.db_config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT employer_title, COUNT(*) AS vacancies_count FROM employers
                    GROUP BY employer_title
                """)
                print(cur.fetchall())

    def get_all_vacancies(self) -> None:
        """
        Функция для получения списка всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию
        :return:
        """
        with psycopg2.connect(**self.db_config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT employer_title, vacancy_name, vacancy_salary_from, vacancy_url
                    FROM employers
                """)
                print(cur.fetchall())

    def get_avg_salary(self) -> None:
        """
        Функция для получения средней зарплаты по вакансиям.
        :return:
        """
        with psycopg2.connect(**self.db_config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT employer_title, AVG(vacancy_salary_from) AS avg_salary
                    FROM employers
                    GROUP BY employer_title
                """)
                print(cur.fetchall())

    def get_vacancies_with_higher_salary(self) -> None:
        """
        Функция для получения списка всех вакансий, у которых зарплата выше средней по всем вакансиям.
        :return:
        """
        with psycopg2.connect(**self.db_config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT employer_title, vacancy_name, vacancy_url, vacancy_salary_from
                    FROM employers
                    WHERE vacancy_salary_from > (SELECT AVG(vacancy_salary_from) FROM employers)
                """)
                print(cur.fetchall())

    def get_vacancies_with_keyword(self, sort_word: str) -> None:
        """
        Функция для получения списка всех вакансий с сортировкой по указанному значению (слову)
        :param sort_word: слово-фильтр
        :return:
        """
        with psycopg2.connect(**self.db_config) as conn:
            with conn.cursor() as cur:
                cur.execute(f"""
                    SELECT *
                    FROM employers
                    WHERE vacancy_name LIKE '%{sort_word[1:-1]}%'
                """)
                print(cur.fetchall())
