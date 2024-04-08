class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        #print("The node values are {}".format(self.value))
        
class LinkedList:
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
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self, value): #add value field as youre adding data to the method
        new_node = Node(value) #createing an object which will take the data and pass onto the Node class
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node # Set next attribute of current tail to the new node
            self.tail = new_node
        self.length +=1
        
    def append_1(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            while self.head is not None:
                self.tail.next = new_node
                self.tail = new_node 
            
            

    
    def pop(self):
        if self.length ==0:
            return None 
        temp = self.head 
        pre = self.head
        while(temp.next):
            pre = temp 
            temp = temp.next
        self.tail = pre 
        self.tail.next = None 
        self.length-=1
        if self.length ==0:
            self.head = None 
            self.tail = None
        return temp.value
        

        
my_linked_list = LinkedList(1)



my_linked_list.append_1(10)

my_linked_list.print_list()

