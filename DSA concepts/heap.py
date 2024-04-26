'''max heap and min heap possible 
parent node address = (i-1)//2 
left child pos = (2*i) + 1 
right child pos = (2*i) + 2 '''
class MaxHeap:
    def __init__(self):
        self.heap = []

    def __left_child(self,index):
        return (2 * index) +1
    
    def __right_child(self,index):
        return (2 * index) + 2
    
    def parent(self,index):
        return (index -1)// 2
    
    def __swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) -1

        while current> 0 and self.heap[current] > self.heap[self.parent(current)]:
            self.__swap(current, self.parent(current))
            current = self.parent(current)

    def remove(self): #only remove item from the top and then rearrange the tree
        if len(self.heap) ==0:
            return None
        
        if len(self.heap) ==1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sink_down(0)

        return max_value
    
    def sink_down(self, index):
        max_index = index 
        while True:
            left_index = self.__left_child(index)
            right_index = self.__right_child(index)

            if left_index< len(self.heap) and self.heap(left_index) > self.heap(max_index):
                max_index = left_index
            
            if right_index< len(self.heap) and self.heap(right_index) > self.heap(max_index):
                max_index = right_index

            if max_index!= index:
                self.__swap(index, max_index)
                index = max_index
            else:
                return      

               
    def print_heap(self):
        print("[", end="")
        for i in range(len(self.heap)):
            print(self.heap[i], end="")
            if i < len(self.heap) - 1:
                print(", ", end="")
        print("]", end="")

my_heap = MaxHeap()
my_heap.insert(98)
my_heap.insert(200)
my_heap.insert(99)
my_heap.insert(20)
my_heap.remove()
my_heap.print_heap()

