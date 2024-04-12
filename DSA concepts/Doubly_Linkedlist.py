class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, "-->", end = " ")
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length ==0:
            return None
        elif self.length ==1:
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None 
        self.length -=1
        return temp

    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head 
            self.head.prev = new_node 
            self.head = new_node
        self.length +=1
        return True
    
    def pop_first(self):
        if self.length ==0:
            return None
        if self.length == 1:
            self.head = None 
            self.tail = None
        else:
            temp = self.head
            self.head = self.head.next 
            self.head.prev = None
            temp.next = None
        self.length -=1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None 
        temp = self.head 
        if index < self.length/2: #first half of the linked list 
            for _ in range(index):
                temp = temp.next 
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False 
    
    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return None
        if index ==0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        else:
            before = self.get(index - 1)
            after = before.next
            new_node.next = after 
            new_node.prev = before
            before.next = new_node
            after.prev = new_node
            return True
        return False
    
    def remove(self,index):
        if index < 0 or index >= self.length:
            return None 
        if index ==0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        else: 
            temp = self.get(index)
            before = self.get(index - 1)
            after = before.next.next
            before.next = after
            after.prev = before
            self.length -=1 
            return True 
        return False
    
    def swap_first_last_p(self):
        if self.head is None or self.head.next is None:
        # Empty list or list with only one element, no need to swap
            return None

        first = self.head
        last = self.tail

        first.next.prev = last 
        last.prev.next = first 
        last.next = first.next 
        last.prev = None 
        first.next = None

        self.head = last 
        self.tail = first 
    
    def swap_first_last(self):
        if self.head is None or self.head == self.tail:
            return None 
        self.head.value,self.tail.value = self.tail.value, self.head.value
    
       
        


    

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)
my_doubly_linked_list.swap_first_last_p()





print('Doubly Linked List:')
my_doubly_linked_list.print_list()