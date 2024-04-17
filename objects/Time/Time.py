class Time:
    def __init__(self):
        self.second = 0.0
        self.minute = 0.0
        self.hour = 0.0
        self.day = 0.0
        self.month = 0.0
        self.months = {
            1: 31,  # January
            2: 28,  # February (29 in leap years)
            3: 31,  # March
            4: 30,  # April
            5: 31,  # May
            6: 30,  # June
            7: 31,  # July
            8: 31,  # August
            9: 30,  # September
            10: 31,  # October
            11: 30,  # November
            12: 31  # December
        }

    def update_time_second(self, time):
        self.second += time
        self.recalculate_time()

    def recalculate_time(self):
        if self.second >= 60:
            self.minute += 1
            self.second = 0

        if self.minute >= 60:
            self.hour +=1
            self.minute = 0

        if self.hour >= 24:
            self.day += 1
            self.hour = 0

        if self.day >= self.months[self.month]:
            self.month += 1
            self.day = 0

        if self.month > 12:
            print("Minął ROK!!!!")