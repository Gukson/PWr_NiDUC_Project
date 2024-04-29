import random
from queue import LifoQueue

from objects.Machines.Section import Section
from objects.Machines.Software import Software
from objects.Pack.Pack import Pack
from objects.Pack.generation import Generation
from objects.Time.Time import Time

class Symulation:
    def run(self):
        file_path = r"./data/Lista-kodów-pocztowych-Excel-2018.xlsx"
        generator = Generation(file_path)
        time = Time()

        stack = LifoQueue()
        # generating data
        for _ in range(500):
            gender = random.choice(['male', 'female'])
            name = generator.generate_name(gender)
            city, postal_code = generator.generate_city_and_postal_code()
            stack.put(Pack(name, postal_code, city))
            print(name, postal_code, city)

        Soft = Software.FirstLetterSort()
        s1 = Section(3, Soft, stack)

        while time.current_time.year != 2:
            s1.update_section()
            time.update_time_second()
            #print(time.current_time.year, time.current_time.month, time.current_time.day, time.current_time.hour, time.current_time.minute, time.current_time.second)
            #TODO RepairTeam ready but not implemented
