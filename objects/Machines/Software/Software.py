# This functions calculates the index where a "Pack" should be dropped in an array.
from queue import LifoQueue


class FirstLetterSort:
    def __init__(self):
        self.__outputContainerSize = 9

    def sort(self, postal_code):
        return int(postal_code[0]) - 1

    def get_output_size(self):
        return self.__outputContainerSize


class SecondLetterSort:
    def __init__(self):
        self.outputContainerSize = 9

    def sort(self, postal_code):
        return int(postal_code[1]) - 1


class PrimaryLetterSort:
    def __init__(self):
        self.outputContainerSize = 2

    def priority_sort(self, flags):
        if "priority" in flags:
            return 0


def generate_output_array(output_container_size):
    output_array = []
    for x in range(0, output_container_size):
        output_array.append(LifoQueue())
    return output_array
