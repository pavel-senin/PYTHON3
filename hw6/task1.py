from datetime import datetime

__all__ = ['check_year', 'date_validator']

def _check_leap_year(date: str) -> bool:
    CHECK_NORMAL_1 = 4
    CHECK_NORMAL_2 = 100
    CHECK_NORMAL_3 = 400
    YEARS = range(1, 10000)
    year = int(date.split(".")[-1])
    if year in YEARS and year % CHECK_NORMAL_1 == 0 and year % CHECK_NORMAL_2 != 0 or year % CHECK_NORMAL_3 == 0:
        return True
    return False


def check_year(year: str) -> bool:
    try:
        _ = datetime.strptime(year, "%d.%m.%Y").date()
        return True
    except ValueError:
        return False


def date_validator(date: str) -> str:
    if check_year(date):
        return 'Високосный' if _check_leap_year(date) else 'Не является высокосным'
    else:
        return f'Дата заполнена некорректно'
    

datoToCheck = "30.11.1999"
print(date_validator(datoToCheck))