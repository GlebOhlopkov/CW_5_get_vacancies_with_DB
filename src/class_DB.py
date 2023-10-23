from utils import config


class DBManager():
    """
    Класс для работы с базой данных PostgreSQL (pgAdmin)
    """

    def __init__(self):
        """
        Создание экземпляра класса для работы с базой данных, указанной в database.ini
        """
        self.db_config: dict = config()
