import json


class Config:
    def __init__(self, durability, effectiveness_rate, monthly_repairs, repair_cost):
        self.__target_durability = durability  # trwałość do której będzie naprawiana maszyna
        self.__effectiveness_rate = effectiveness_rate  # współczynnik skuteczności pracowników
        self.__monthly_repairs = monthly_repairs  # czy co miesięczne naprawy
        self.__repair_cost = repair_cost  # koszt napraw

    # Gettery
    def get_durability(self):
        return self.__target_durability

    def get_effectiveness_rate(self):
        return self.__effectiveness_rate

    def get_monthly_repairs(self):
        return self.__monthly_repairs

    def get_repair_cost(self):
        return self.__repair_cost

    def save_to_json(self, filename):
        config_data = {
            'durability': self.__target_durability,
            'effectiveness_rate': self.__effectiveness_rate,
            'monthly_repairs': self.__monthly_repairs,
            'repair_cost': self.__repair_cost
        }
        with open('data/jsons/'+filename, 'w') as json_file:
            json.dump(config_data, json_file, indent=4)

    @classmethod
    def load_from_json(cls, filename):
        with open(filename, 'r') as json_file:
            config_data = json.load(json_file)
        return cls(**config_data)
