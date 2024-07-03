import json
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='logs/application.log',
                    filemode='w')

logger = logging.getLogger("utils")

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
