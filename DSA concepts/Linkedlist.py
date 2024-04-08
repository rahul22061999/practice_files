class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
                
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, "-->", end=" ")
            temp = temp.next
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
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
        
    def add_beg(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def del_first(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            self.head = self.head.next
    
    def del_first_test(self):
        n = self.head
        n = n.next
        self.head = n

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
    
    def pop_1(self):
        if self.head is None:
            print("No value")
        elif self.head.next is None:
            self.head = None
            self.tail = None
        else:
            n = self.head 
            while n.next.next:
                n = n.next
            n.next = None
            self.tail = n
    
    def del_by_value(self, x):
        if self.head is None:
            return None
        elif x == self.head.value:
            self.head = self.head.next
            return
        n = self.head
        while n.next is not None:
            if x == n.next.value:
                n.next = n.next.next
                return
            n = n.next
        print("Value not found in the list.")
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value

    def set_value(self, index, value):
        new_node = Node(value)
        if index < 0 or index >= self.length:
            return False
        n = self.head
        for _ in range(index):
            n = n.next
        n.value = value
        return True
    
    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index >= self.length:
            return False
        if index ==0:
            return self.prepend(value)
        if index == self.length :
            return self.append(value)
        n = self.head 
        m = self.head
        for _ in range(index -1):
            n = n.next
        for _ in range(index +1):
            m = m.next
        n.next = new_node
        new_node = n
        n.next.next = m
        #print(n.value, m.value)
    
    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        n = self.head 
        m = self.head
        for _ in range(index -1):
            n = n.next
        for _ in range(index +1):
            m = m.next
        n.next = new_node
        new_node = n
        n.next.next = m
        return True
        #print(n.value, m.value)

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
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
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
        
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def find_middle_node(self):
        if self.head is None:
            return None
        
        slow = self.head
        fast = self.head
    
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
    
        # If the list has an even number of nodes, return the first node of the second half
        if fast.next is None:
            return slow.next.value
        else:
            return slow.value
        


# Create a linked list with 3 nodes
linked_list = LinkedList(5)
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
#linked_list.insert(1,17)
linked_list.remove(5)
linked_list.find_middle_node()


#my_linked_list.add_beg(100)
#my_linked_list.pop_1()

  
#my_linked_list.del_first_test()

print(linked_list.find_middle_node())

