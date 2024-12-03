import logging
import days


logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":
    for day in [
        days.DayOne,
        days.DayTwo,
    ]:
        day()

