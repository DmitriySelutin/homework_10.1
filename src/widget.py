from src.masks import get_mask_account, get_mask_card


def mask_account_card(number: str) -> str:
    """Функция принимает строку и маскирует номер карты или счета"""
    if len(number.split()[-1]) == 16:
        mask_card = get_mask_card(number.split()[-1])
        result = f"{number[:-16]}{mask_card}"
    elif len(number.split()[-1]) == 20:
        mask_card = get_mask_account(number.split()[-1])
        result = f"{number[:-21]}{mask_card}"
    return result


def get_user_data(old_data: str) -> str:
    """Функция принимает строку с датой и форматирует ее"""
    data_reverse = old_data[0:10].split("-")
    return ".".join(data_reverse[::-1])
