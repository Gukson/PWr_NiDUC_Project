import random
from queue import LifoQueue

from objects.Machines.Section import Section
from objects.Machines.Software import Software
from objects.Pack.Pack import Pack
from objects.Pack.generation import Generation
from objects.Time.Time import Time
from objects.Repair_team.Repair_team import Repair_team
from objects.Repair_team.Config import Config


class Symulation:
    def run(self, config: Config):
        file_path = r"./data/Lista-kodów-pocztowych-Excel-2018.xlsx"
        generator = Generation(file_path)
        time = Time()
        repair_team = Repair_team(time, config)
        stack = LifoQueue()

        # generating data
        for _ in range(508):
            gender = random.choice(['male', 'female'])
            name = generator.generate_name(gender)
            city, postal_code = generator.generate_city_and_postal_code()
            stack.put(Pack(name, postal_code, city))
            print(name, postal_code, city)

        Soft = Software.SortingSoftware()
        s1 = Section(1, Soft, stack, time,100,repair_team)

        #temponary variable
        current_month = time.current_time.month

        while time.current_time.year != 2 and stack.empty() == False :
            if config.get_monthly_repairs() and current_month != time.current_time.month:
                repair_team.monthly_repair(s1.machines)

            s1.update_section()
            repair_team.update()
            time.update_time_miliseconds(20)
