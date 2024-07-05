import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="logs/application.log",
    filemode="w",
)

logger = logging.getLogger("masks")


def get_mask_card(number: str) -> str:
    """Функция принимает строку и возвращает маску карты"""
    logger.info(f"Принимаем номер карты: {number}")
    new_string = f"{number[0:4]} {number[4:6]}** **** {number[12:]}"
    return new_string


def get_mask_account(number: str) -> str:
    """Функция принимает строку и возвращает маску счёта"""
    new_string = f"**{number[-4::]}"
    return new_string
