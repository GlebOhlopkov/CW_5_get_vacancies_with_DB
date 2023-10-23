from configparser import ConfigParser

import json


def config(filename="database.ini", section="postgresql") -> dict:
    """
    Функция для формирования словаря с параметрами для подключения к базе данных
    :param filename: имя файла с данными базы данных
    :param section: тип полей для заполнения
    :return: словарь с параметрами для подключения к базе данных
    """
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} is not found in the {1} file.'.format(section, filename))
    return db


def load_employers(json_file) -> dict:
    """
    Функция для формирования словаря с данными необходимых компаний
    :param json_file: имя файла с данными компаний
    :return: словарь с данными компаний (имя, id)
    """
    with open(json_file, 'r', encoding='utf-8') as file:
        return json.load(file)
