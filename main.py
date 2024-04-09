from objects.Pack.generation import Generation
from queue import LifoQueue
from objects.Pack.Pack import Pack
import random

if __name__ == "__main__":
    file_path = r"./data/Lista-kodów-pocztowych-Excel-2018.xlsx"
    generator = Generation(file_path)

    stack = LifoQueue()
    #generating data
    for _ in range(5):
        gender = random.choice(['male', 'female'])
        name = generator.generate_name(gender)
        city, postal_code = generator.generate_city_and_postal_code()
        stack.put(Pack(name, postal_code, city))
        print(name, postal_code, city)