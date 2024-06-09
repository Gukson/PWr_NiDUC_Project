import datetime

from objects.Repair_team.Config import Config


class Repair_team:
    def __init__(self, time, config: Config):
        self.processes = {}
        self.time = time
        self.config = config
        self.up_to = config.get_durability()

    #założenie jest takie, że naprawa do 80% jest szybsza niż powyżej 80%
    def calculate_repair_end_time(self, current_durability, expected_durability):
        if expected_durability <= 80:
            time_in_hours = (expected_durability - current_durability) * 0.05 * 1 / self.config.get_effectiveness_rate()
        else:
            over_80 = expected_durability - 80
            time_in_hours = (
                                        expected_durability - current_durability - over_80) * 0.5 * 1 / self.config.get_effectiveness_rate()
            time_in_hours += over_80 * 0.1 * 1 / self.config.get_effectiveness_rate()

        print(f"{self.time.current_time}\n")
        print(f"{self.time.current_time + datetime.timedelta(hours=time_in_hours)}\n")
        return self.time.current_time + datetime.timedelta(hours=time_in_hours)

    def repair(self, machine):
        print(f"naprawa maszyny {machine.id}")
        self.processes.update({machine: [self.calculate_repair_end_time(machine.durability, self.up_to), self.up_to]})
        machine.active = False

    def update(self):
        list = []
        for machine in self.processes.keys():
            if self.processes[machine][0] <= self.time.current_time:
                machine.durability = self.processes[machine][1]
                list.append(machine)
                machine.active = True
        for machine in list:
            del self.processes[machine]

    def monthly_repair(self, machines):
        for machine in machines:
            if not machine.active:
                machine.active = False
                self.repair(machine)
