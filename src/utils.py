import json


def get_transactions(file_path):
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с
    данными о финансовых транзакциях. Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            response = json.load(file)
            if isinstance(response, list):
                return response
            else:
                return []
    except Exception as e:
        print(f"Ошибка {e}")
        return []
