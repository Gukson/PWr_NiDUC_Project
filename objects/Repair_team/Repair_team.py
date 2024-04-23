from objects.Machines.Machine import Machine
from objects.Time.Time import Time
class Repair_team:
    def __init__(self, time, work_efficiency):
        self.processes = {}
        self.work_efficiency = work_efficiency
        self.time = time


    def calculate_repair_end_time(self, current_durability, expected_durability):
        end_time = self.time.current_time


    def repair(self, machine: Machine, up_to: int):
        # self.processes.update({machine: })
        print("WIP")

