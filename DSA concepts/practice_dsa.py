def append(self, data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        self.tail = new_node
    else:
        while self.head is not None:
            self.tail.next = new_node
            self.tail = new_node 
        
            
