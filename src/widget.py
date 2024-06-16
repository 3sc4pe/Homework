import masks


def mask_account_card(string: str) -> str:
    """Функция для маскировки счетев и карт """
    if "Счет" in string:
        account = string[-20:]
        return string[:20] + masks.get_mask_account(account)
    else:
        number_card = "".join(string[-16:].split())
        return string[:-16] + masks.get_mask_card_number(number_card)


# print(mask_account_card('Maestro:1596837868705122422'))

def get_data(info_data: str) -> str:
    """Фунция преоброзования даты и времени"""
    data_day = info_data.split("T")[0]

    return f"{data_day.split('-')[-1]}.{data_day.split('-')[-2]}.{data_day.split('-')[-3]}"


# print(get_data('2018-07-11T02:26:18.671407'))
