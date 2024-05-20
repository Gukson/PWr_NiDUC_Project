import datetime
class Time:
    def __init__(self):
        self.current_time = datetime.datetime(1,1,1,0,0,0)

    def update_time_miliseconds(self, amount):
        self.current_time += datetime.timedelta(milliseconds=amount)
    def update_time_second(self):
        self.current_time += datetime.timedelta(seconds=1)

    def update_time_hours(self, amount):
        self.current_time += datetime.timedelta(hours=amount)

    def get_current_time(self):
        return self.current_time