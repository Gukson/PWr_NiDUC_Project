# symulacja Monte Carlo czasu przetwarzania paczek

import random
import matplotlib.pyplot as plt
from objects.Pack.Pack import Pack
from objects.Machines.Machine import Machine
from objects.Time.Time import Time

def monte_carlo_simulation(num_packages, num_iterations):
    processing_times = []

    for _ in range(num_iterations):
        total_time = 0
        input_stack = []
        for _ in range(num_packages):
            name = "Example Name"
            postal_code = "12345"
            city = "Example City"
            pack = Pack(name, postal_code, city)
            input_stack.append(pack)

        output_container = [None] * 100  # Założenie: output_container ma 100 miejsc
        time = Time() 
        machine = Machine(100, None, input_stack, output_container, 0, time, None)  

        for pack in input_stack:
            processing_time = random.uniform(0.5, 2.5) 
            total_time += processing_time

        processing_times.append(total_time)

    return processing_times

num_packages = 100  
num_iterations = 1000 

processing_times = monte_carlo_simulation(num_packages, num_iterations)

# Wykres histogramu czasu przetwarzania paczek
plt.hist(processing_times, bins=30, edgecolor='black')
plt.xlabel('Czas przetwarzania [min]')
plt.ylabel('Liczba symulacji')
plt.title('Histogram czasu przetwarzania paczek')
plt.show()

# Wykres gęstości prawdopodobieństwa czasu przetwarzania
'''
plt.hist(processing_times, bins=30, density=True, alpha=0.6, color='g', edgecolor='black')
plt.xlabel('Czas przetwarzania [min]')
plt.ylabel('Gęstość prawdopodobieństwa')
plt.title('Gęstość prawdopodobieństwa czasu przetwarzania paczek')
plt.show()
'''

# Wykres pudełkowy czasu przetwarzania
plt.boxplot(processing_times)
plt.ylabel('Czas przetwarzania [min]')
plt.title('Wykres pudełkowy czasu przetwarzania paczek')
plt.show()
