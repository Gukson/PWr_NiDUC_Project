from objects.Machines.Machine import Machine
from objects.Machines.Software import Software



class Section:
    def __init__(self, amount, soft, input_data, time, durability, repair_team):
        self.amount = amount
        self.soft = soft
        self.input_data = input_data
        self.machines = []
        self.time = time
        self.durability = durability
        self.repairTeam = repair_team

        self.output_container = Software.generate_output_array(self.soft.get_output_size())

        for x in range(0, amount):
            self.machines.append(Machine(self.durability, self.soft, self.input_data, self.output_container, x,self.time,repair_team))

    def update_section(self):
        for machine in self.machines:
            machine.sort()

