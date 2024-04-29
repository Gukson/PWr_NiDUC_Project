import datetime

from objects.Machines.Machine import Machine
class Repair_team:
    def __init__(self, time, work_efficiency):
        self.processes = {}
        self.work_efficiency = work_efficiency
        self.time = time


    #założenie jest takie, że naprawa do 80% jest szybsza niż powyżej 80%
    def calculate_repair_end_time(self, current_durability, expected_durability):

        if expected_durability <= 80:
            time_in_hours = (expected_durability - current_durability) * 0.5 * 1/self.work_efficiency
        else:
            over_80 = expected_durability - 80
            time_in_hours = (expected_durability - current_durability - over_80) * 0.5 * 1/self.work_efficiency
            time_in_hours += over_80 * 0.75 * 1/self.work_efficiency
        return self.time.current_time + datetime.timedelta(hours=time_in_hours)

    def repair(self, machine: Machine, up_to: int):
        self.processes.update({machine:[self.calculate_repair_end_time(machine.durability,up_to),up_to]})

    def update(self):
        for machine in self.processes.keys():
            if self.processes[machine][0] <= self.time.current_time:
                machine.durability = self.processes[machine][1]

