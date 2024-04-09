from objects.Machines.Machine import Machine
from Software import Software

class Section:
    def __init__(self, amount, software, input_data):
        self.amount = amount
        self.software = software
        self.input_data = input_data

        output_container = Software.__generate_output_array(software.outputContainerSize)
        machines = []

        for x in range(0, amount):
            machines.append(Machine(1000, 1.0, self.software, self.input_data, output_container))