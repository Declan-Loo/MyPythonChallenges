class Node:
    #Initialise the node (data/next pointer which points to the next node).
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
     #Initialise Linked List heads
    def __init__(self):
        self.head = None
    #Function to insert new nodes into linked list
    def insert(self, data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current=  current.next
            current.next = new_node
        else:
            self.head = new_node
    #Function to find a particular data in the linked list
    def find(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return current
            current = current.next
        return None
    #Function to delete a node
    def delete(self, data):
        current = self.head
        previous = None
        while current is not None:
            if current.data == data:
                if previous is not None:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True
            previous = current
            current = current.next
        return False
    #Function to print the linked list
    def printList(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next
    
linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert("B")
linked_list.insert(3)
linked_list.printList()
