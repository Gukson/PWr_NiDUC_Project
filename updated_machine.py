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
        
class Software:
    def sort(self, post_code):
        container_number = int(post_code) % 10 
        return container_number
           
def main():
    
    class Stack:
        def __init__(self):
            self.items = []

        def put(self, item):
            self.items.append(item)

        def get(self):
            return self.items.pop()

    class Container:
        def __init__(self, capacity):
            self.capacity = capacity
            self.items = []

        def put(self, item):
            if len(self.items) < self.capacity:
                self.items.append(item)
            else:
                print("Container is full. Discarding item:", item)

    # maszyny
    machine1 = Machine(durability=100, operatingtime=60, software=Software(), input_stack=Stack(), output_container=Container(10), id=1)
    machine2 = Machine(durability=120, operatingtime=45, software=Software(), input_stack=Stack(), output_container=Container(10), id=2)

    for i in range(20):
        package = Pack(postal_code=str(i)) 
        machine1.input_stack.put(package)

    for _ in range(70):
        machine1.sort()
        
    for _ in range(70):
        machine2.sort()

if __name__ == "__main__":
    main()

