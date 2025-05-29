class linkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data,self.head)
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

class Node :
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
lista = linkedList() #nudo al principio
lista.insert(1)
lista.insert(2)
lista.insert(3)
lista.print_list()     
        
