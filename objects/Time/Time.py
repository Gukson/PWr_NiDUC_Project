import datetime
class Time:
    def __init__(self):
        self.current_time = datetime.datetime(1,1,1,0,0,0)

    def update_time_second(self):
        self.current_time += datetime.timedelta(seconds=1)