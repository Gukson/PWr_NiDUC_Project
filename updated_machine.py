import time

class Machine:
    def __init__(self, durability, operatingtime, software, input_stack, output_container, id):
        self.initial_durability = durability
        self.durability = durability
        self.operatingtime = operatingtime
        self.software = software
        self.input_stack = input_stack
        self.output_container = output_container
        self.id = id
        self.start_time = time.time()
        self.active = True

    def set_input_stack(self, input_stack):
        self.input_stack = input_stack

    def sort(self):
        if not self.active:
            print("Machine %d is deactivated." % self.id)
            return

        #tutaj czas podmienić
        current_time = time.time()
        elapsed_time = current_time - self.start_time
        remaining_time = self.operatingtime - elapsed_time
        if remaining_time <= 0:
            print("Machine %d has exceeded operating time." % self.id)
            self.deactivate()
            return

        pack = self.input_stack.get()
        pos = self.software.sort(pack.get_post_code())
        self.output_container[pos].put(pack)

        durability_ratio = elapsed_time / self.operatingtime
        self.durability = self.initial_durability - (self.initial_durability * durability_ratio)

        print("Durability: %d %d " % (self.durability, self.id))
        if self.durability <= 0:
            self.deactivate()
            print("Machine %d has reached 0 durability and is deactivated." % self.id)
            return
        
        # ekipa z poznania lub krakowa ?

        time.sleep(0.05)

    def deactivate(self):
        self.active = False
