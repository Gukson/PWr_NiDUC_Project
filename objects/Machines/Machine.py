import datetime
from objects.Pack.Pack import Pack


class Machine:
    def __init__(self, durability, software, input_stack, output_container, id, time):
        self.initial_durability = durability
        self.durability = durability
        self.operating_time = 0
        self.software = software
        self.input_stack = input_stack
        self.output_container = output_container
        self.id = id
        self.time = time
        self.start_time = time.get_current_time()
        self.active = True
        self.status = "waiting"
        self.pack = Pack

    def set_input_stack(self, input_stack):
        self.input_stack = input_stack

    def sort(self):
        if not self.active:
            # print("Machine %d is deactivated." % self.id)
            return

        if self.status == "waiting" and self.durability > 0:
            if not self.input_stack.empty():
                self.start_time = self.time.get_current_time()
                self.operating_time = self.calculate_operating_time(self.durability / self.initial_durability)
                self.status = "running"
                self.pack = self.input_stack.get()
            return

        if self.status == "running" and self.durability > 0:
            if self.time.get_current_time() >= self.start_time + datetime.timedelta(milliseconds=self.operating_time):
                pos = self.software.sort(self.pack.get_post_code())
                self.output_container[pos].put(self.pack)
                self.durability -= 1
                print("Durability: %d %d " % (self.durability, self.id))
                self.status = "waiting"
                return

        if self.durability <= 0:
            self.deactivate()
            print("Machine %d has reached 0 durability and is deactivated." % self.id)
            return


    def deactivate(self):
        self.active = False

    def calculate_operating_time(self, durability):
        if durability > 80:
            return 62
        elif durability > 50:
            return 75
        elif durability > 30:
            return 82
        else:
            return 90
