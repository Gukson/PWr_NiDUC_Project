import datetime

class Time:
    def __init__(self):
        self.current_time = datetime.datetime(1, 1, 1, 0, 0, 0)

    def update_time_milliseconds(self, amount):
        self.current_time += datetime.timedelta(milliseconds=amount)

    def update_time_seconds(self, amount):
        self.current_time += datetime.timedelta(seconds=amount)

    def update_time_hours(self, amount):
        self.current_time += datetime.timedelta(hours=amount)

    def get_current_time(self):
        return self.current_time
