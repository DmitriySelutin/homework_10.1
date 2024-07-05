import csv
import json
import os

import pandas as pd
from src.logger import setup_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_1 = os.path.join(current_dir, "../logs", "utils.log")

logger = setup_logger("utils", file_path_1)


def get_transactions(file_path):
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с
    данными о финансовых транзакциях. Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            response = json.load(file)
            if isinstance(response, list):
                logger.info("Возвращает список словарей")
                return response
            else:
                logger.info("Файл пустой,содержит не список или не найден")
                return []
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")
        print(f"Ошибка {e}")
        return []


def get_transactions_csv(file_path):
    data_list = []
    logger.info(f"Чтение файла {file_path}")
    with open(file_path, "r", encoding="utf-8") as file:
        transactions_reader = csv.DictReader(file, delimiter=";")
        for row in transactions_reader:
            data_list.append(row)
        logger.info("Возвращает список словарей")
        return data_list


def get_transactions_excel(file_path):
    logger.info(f"Чтение файла {file_path}")
    with open(file_path, "rb") as file:
        df_excel = pd.read_excel(file)
        list_of_dicts = df_excel.to_dict("records")
        logger.info("Возвращает список словарей")
        return list_of_dicts
