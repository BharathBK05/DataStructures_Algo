class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next : Node| None = None

class Linkedlist():

    def __init__(self):
        self.head = None
        self.tail = None

    def insertEnd(self,data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
            
        else:
            self.head = new_node
            self.tail = new_node

    def insertHead(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head  
            self.head = new_node          

    def display(self):

        temp = self.head

        if temp:

            while temp.next != None:
                print(temp.data, end = ' ')
                print('-->', end = ' ')
                temp = temp.next

            print(temp.data)    

    def deleteEnd(self):

        temp = self.head

        if temp:

            while temp.next != self.tail:
                temp = temp.next

            temp.next.data = None #deallocate the memory for removed node
            temp.next = None
            self.tail = temp


if __name__ == '__main__':
    try:
        single = Linkedlist()
        single.insertEnd(10)
        single.insertEnd(20)
        single.display()
        single.deleteEnd()
        single.insertHead(40)
        single.display()


    except Exception as e:
        print(e)    