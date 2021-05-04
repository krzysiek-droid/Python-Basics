import datetime


class clock_date:
    def __init__(self, zoneUTC):
        self.zone = zoneUTC
    pass


class clock(clock_date):
    def time(self):
        print(datetime.datetime.now())
    pass


class date(clock_date, clock):
    def show_date(self):
        print(f"Actual date is: {datetime.date.today()}")
    pass


if __name__ == "__main__":
    warsaw = clock_date("+1")
    warsaw.show_date()
    warsaw.time()