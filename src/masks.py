def get_mask_card_number(number: str) -> str:
    """Функция, которая  возвращает маскированный номер карты"""
    new_num = str(number)
    if len(new_num) == 16:
        return f"{new_num[:4]} {new_num[4:6]}** **** {new_num[12:]}"


def get_mask_account(number: str) -> str:
    """Функция, которая возвращает маскированный номер счета"""
    new_num = str(number)
    if len(new_num) == 20:
        return f"**{new_num[-4:]}"
