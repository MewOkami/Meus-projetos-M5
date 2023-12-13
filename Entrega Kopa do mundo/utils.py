from exceptions import NegativeTitlesError
from exceptions import InvalidYearCupError
from exceptions import ImpossibleTitlesError


def data_processing(data):

    title = data["titles"]
    if title < 0:
        raise NegativeTitlesError("titles cannot be negative")

    first_cup = data["first_cup"]

    first_cup_year = int(first_cup[:4])

    if first_cup_year < 1930 or (first_cup_year - 1930) % 4 != 0:
        raise InvalidYearCupError("there was no world cup this year")

    title = data["titles"]
    first_cup = data["first_cup"]

    first_cup_year = int(first_cup[:4])

    if title < 0 or title > (2023 - first_cup_year) // 4:
        raise ImpossibleTitlesError(
            "impossible to have more titles than disputed cups")
