import csv
import json
import os
import re

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


def get_transactions_filter_by_key(transactions, search_key):
    """Функция, которая будет принимать список словарей с данными о банковских операциях и строку поиска,
    а возвращать список словарей."""
    result = []
    for transaction in transactions:
        if "description" in transaction and re.search(search_key, transaction["description"], re.IGNORECASE):
            result.append(transaction)
    return result


def get_transactions_by_category(transactions: list[dict], categories: dict) -> dict:
    """
    Принимает список словарей с данными о банковских операциях и словарь категорий операций.
    Возвращает словарь, в котором ключи - это названия категорий, а значения - количество операций в каждой категории.
    """

    category_counts = {category: 0 for category in categories}

    for transaction in transactions:
        if "description" in transaction:
            for category in categories:
                if category.lower() in transaction["description"].lower():
                    category_counts[category] += 1

    return category_counts


def get_transactions_filter_by_rub(transactions: list, search_key: str) -> list:
    """Функция фильтрации транзакций по коду валюты"""
    result = []
    for transaction in transactions:
        if (
            "operationAmount" in transaction
            and "currency" in transaction["operationAmount"]
            and re.search(search_key, transaction["operationAmount"]["currency"]["code"], re.IGNORECASE)
        ):
            result.append(transaction)
    return result


def get_transactions_filter_by_rub_csv(transactions: list, search_code: str) -> list:
    """Функция фильтрации транзакций по коду валюты"""
    result = []
    for transaction in transactions:
        if "currency_code" in transaction and re.search(search_code, transaction["currency_code"], re.IGNORECASE):
            result.append(transaction)
    return result


def get_transactions_filter_by_rub_xlsx(transactions: list, search_code: str) -> list:
    """Функция фильтрации транзакций по коду валюты"""
    result = []
    for transaction in transactions:
        if pd.notnull(transaction["currency_code"]) and re.search(
            search_code, transaction["currency_code"], re.IGNORECASE
        ):
            result.append(transaction)
    return result


#
# current_dir = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(current_dir, "../data", "transactions_excel.xlsx")
# transactions = get_transactions_excel(file_path)
#
#
# transaction = get_transactions_filter_by_rub_xlsx(transactions, "RUB")
# print(transaction)
