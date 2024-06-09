# symulacja Monte Carlo zużycia maszyn

import random
from queue import LifoQueue
from objects.Machines.Section import Section
from objects.Machines.Software import Software
from objects.Pack.Pack import Pack
from objects.Pack.generation import Generation
from objects.Time.Time import Time
from objects.Repair_team.Repair_team import Repair_team
from objects.Repair_team.Config import Config
import matplotlib.pyplot as plt

class MonteCarloSimulation:
    def __init__(self, config, num_simulations):
        self.config = config
        self.num_simulations = num_simulations
        self.results = []

    def run_simulation(self):
        file_path = r"./data/Lista-kodów-pocztowych-Excel-2018.xlsx"
        generator = Generation(file_path)
        
        for sim_num in range(self.num_simulations):
            print(f"Starting simulation {sim_num+1}...")
            time = Time()
            repair_team = Repair_team(time, self.config)
            stack = LifoQueue()

            for _ in range(508):
                gender = random.choice(['male', 'female'])
                name = generator.generate_name(gender)
                city, postal_code = generator.generate_city_and_postal_code()
                stack.put(Pack(name, postal_code, city))

            software = Software.SortingSoftware()
            section = Section(1, software, stack, time, 100, repair_team)
            initial_durability = section.machines[0].durability

            max_iterations = 10000
            iterations = 0

            while time.get_current_time().year != 2 and not stack.empty() and iterations < max_iterations:
                section.update_section()
                repair_team.update()
                time.update_time_seconds(1) 
                iterations += 1

                print(f"Iteration {iterations}, Time: {time.get_current_time()}, Durability: {section.machines[0].durability}, Stack Empty: {stack.empty()}")

                if all(machine.durability == 0 for machine in section.machines):
                    print(f"All machines deactivated. Stopping simulation {sim_num+1}.")
                    break

            if iterations >= max_iterations:
                print("Reached maximum iterations. Exiting loop.")
                
            final_durability = section.machines[0].durability
            durability_loss = initial_durability - final_durability
            self.results.append(durability_loss)

    def plot_results(self):
        print("Results:", self.results)
        
        plt.hist(self.results, bins=30, edgecolor='k')
        plt.title('Rozkład utraty wytrzymałości po 1 roku')
        plt.xlabel('Utrata wytrzymałości')
        plt.ylabel('Częstotliwość')
        plt.show()

if __name__ == "__main__":
    config = Config(80, 1, True, 100)
    num_simulations = 1000

    simulation = MonteCarloSimulation(config, num_simulations)
    simulation.run_simulation()
    simulation.plot_results()
