import time
class Machine:
    def __init__(self, durability, speed, software,input_stack, output_container, id):
        self.durability = durability
        self.speed = speed
        self.software = software
        self.input_stack = input_stack
        self.output_container = output_container
        self.id = id

    def set_input_stack(self, input_stack):
        self.input_stack = input_stack

    def sort(self):
        pack = self.input_stack.get()
        pos = self.software.sort(pack.get_post_code())
        self.output_container[pos].put(pack)
        self.durability -= 1
        print("Durability: %d %d ",  self.durability, self.id)
        # time.sleep(0.05)