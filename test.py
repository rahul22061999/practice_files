class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    def pop(self):
        if self.length == 0:
            return None 
        temp = self.head 
        pre = self.head
        while temp.next:
            pre = temp 
            temp = temp.next
        self.tail = pre 
        self.tail.next = None 
        self.length -= 1
        if self.length == 0:
            self.head = None 
            self.tail = None
        return temp.value
    def print_list(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    
                    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        n = self.get(index - 1)
        new_node.next = n.next
        n.next = new_node
        self.length += 1   
        return True  
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def remove(self,x):
        if x == self.head.value:
            return self.pop_first()
        if x == self.length:
            return self.pop()
        


# Create a linked list with 3 nodes
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.insert(0,5)
linked_list.remove(5)
# Illustrate the difference between self.head.next and self.next
print(linked_list.print_list())



