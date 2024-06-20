def filter_by_state(dictionary_list: list, state: str = "EXECUTED") -> list:
    """Принимает словари и возвращает новый список из переданных значений"""
    new_list = []
    for i in dictionary_list:
        if i.get("state") == state:
            new_list.append(i)
        elif i.get("state") != state:
            new_list.append(i)
    return new_list


def sort_by_date(date_list: list[dict], reverse_list: bool) -> list:
    """Функция для сортировки полученных значений"""
    sorted_list = sorted(date_list, key=lambda d: d["date"])
    return sorted_list


print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)
