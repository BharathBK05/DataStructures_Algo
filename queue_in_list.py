"""Queue represented by a Python list"""
class Queue:
    def __init__(self):
        self.entries = []
        self.length = 0
        self.front = 0

    def __str__(self):
        printed = "<" + str(self.entries)[1:-1] + ">"
        return printed

    """Enqueues item into queue"""

    def put(self, item):
        self.entries.append(item)
        self.length = self.length + 1

    """Dequeues item from queue"""

    def get(self):
        self.length = self.length - 1
        dequeued = self.entries[self.front]
        self.entries = self.entries[1:]
        return dequeued

    """Rotates the queue """

    def rotate(self, rotation):
        for _ in range(rotation):
            self.put(self.get())



    def get_front(self):
        return self.entries[0]

    """Returns the length of this.entries"""

    def size(self):
        return self.length

def main() -> None:
    queue = Queue()
    queue.put(10)
    queue.put(20)
    print(queue.__str__())
    print("Popped = " + str(queue.get()))
    print(queue.size())
       
    

if __name__ == "__main__":
    main()
