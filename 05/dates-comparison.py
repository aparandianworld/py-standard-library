from datetime import date, time, timedelta


def compare_dates(date1: date, date2: date) -> (bool, float):
    if date1 < date2:
        return True, (date1 - date2).total_seconds()
    if date1 > date2:
        return False, (date2 - date1).total_seconds()
    return None, 0


def main():
    date1 = date(2027, 1, 1)
    date2 = date(2027, 4, 1)

    result, diff = compare_dates(date1, date2)
    print(result, diff)


if __name__ == "__main__":
    main()
