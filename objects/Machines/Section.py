from objects.Machines.Machine import Machine
from objects.Machines.Software import Software
from objects.Time.Time import Time


class Section:
    def __init__(self, amount, soft, input_data):
        self.amount = amount
        self.soft = soft
        self.input_data = input_data
        self.machines = []

        self.output_container = Software.generate_output_array(self.soft.get_output_size())

        for x in range(0, amount):
            self.machines.append(Machine(1000, 1.0, self.soft, self.input_data, self.output_container, x))

    def update_section(self):
        for machine in self.machines:
            machine.sort()


