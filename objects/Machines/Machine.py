class Machine:
    def __init__(self, durability, speed, software,input_stack, output_container):
        self.durability = durability
        self.speed = speed
        self.software = software
        self.input_stack = input_stack
        self.output_container = output_container


    def set_input_stack(self, input_stack):
        self.input_stack = input_stack

    def sort(self):
        while not self.input_stack.empty():
            p = self.input_stack.get()
            pos = self.software(p)
            self.output_container[pos].put(p)
            self.durability -= 1