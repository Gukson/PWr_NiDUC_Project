# symulacja Monte Carlo kosztów

import random
import matplotlib.pyplot as plt
from objects.Machines.Section import Section
from objects.Machines.Software import Software
from objects.Pack.Pack import Pack
from objects.Pack.generation import Generation
from objects.Time.Time import Time
from objects.Repair_team.Repair_team import Repair_team
from objects.Repair_team.Config import Config
from queue import LifoQueue

class OperationalCostSimulation:
    def __init__(self, config: Config):
        self.config = config
        self.time = Time()
        self.repair_team = Repair_team(self.time, config)
        self.stack = self.generate_pack_stack()
        self.section = Section(1, Software.SortingSoftware(), self.stack, self.time, 100, self.repair_team)
        self.operational_costs = []
        self.repair_costs = []

    def generate_pack_stack(self):
        file_path = r"./data/Lista-kodów-pocztowych-Excel-2018.xlsx"
        generator = Generation(file_path)
        stack = LifoQueue()

        for _ in range(508):
            gender = random.choice(['male', 'female'])
            name = generator.generate_name(gender)
            city, postal_code = generator.generate_city_and_postal_code()
            stack.put(Pack(name, postal_code, city))
            print(name, postal_code, city)

        return stack

    def run(self, duration_months):
        while self.time.current_time.year != 2 and not self.stack.empty():
            current_month = self.time.current_time.month

            if self.config.get_monthly_repairs():
                repair_cost = self.repair_team.monthly_repair(self.section.machines)
                self.repair_costs.append(repair_cost)

            operational_cost = self.calculate_operational_cost()
            self.operational_costs.append(operational_cost)

            self.section.update_section()
            self.repair_team.update()
            self.time.update_time_milliseconds(20)

        self.plot_costs()

    def calculate_operational_cost(self):
        # Koszty energii 
        energy_cost_per_hour = 0.15 
        energy_consumption_per_hour = 5000 
        energy_cost = energy_cost_per_hour * energy_consumption_per_hour

        # Koszty pracy
        average_hourly_wage = 20  
        number_of_employees = 10  
        work_hours_per_day = 8  
        work_days_per_month = 22  
        labor_cost = average_hourly_wage * number_of_employees * work_hours_per_day * work_days_per_month

        total_operational_cost = energy_cost + labor_cost
        return total_operational_cost

    def plot_costs(self):
        months = range(1, len(self.operational_costs) + 1)
        plt.plot(months, self.operational_costs, label='Koszty operacyjne')
        plt.plot(months, self.repair_costs, label='Koszty napraw')
        plt.xlabel('Miesiące')
        plt.ylabel('Koszt')
        plt.title('Miesięczne koszty w czasie')
        plt.legend()
        plt.show()

config = Config(80, 1, True, 100)

simulation = OperationalCostSimulation(config)
simulation.run(duration_months=24)
