import logging
from days.day_1 import DayOne


logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":
    for day in [
        DayOne,
    ]:
        day()

