class FIFO_Queue:
    def __init__(self, queue):
        self.queue = list(queue)

    def screen_out(self):
        print(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    def put(self, element):
        self.queue.append(element)

    def get(self):
        try:
            return self.queue.pop(0)
        except IndexError:
            print('Your queue is empty.')

backpack = FIFO_Queue(["apple", "bread", "snack", "compass"])

backpack.put("water")

backpack.screen_out()
print(backpack.get())
backpack.screen_out()
print(backpack.get())
print(backpack.get())
