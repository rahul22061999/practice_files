class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    
    # create hash method

    def hash(self, key):
        my_hash = 0 
        for letter in key:
            # ord(letter) is the ascii value and 23 is prime
            # overall returns remainder which is from 0 to 6
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
            return my_hash
        
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key,value):
        index = self.hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = [] 
        self.data_map[index].append([key,value])

    def get_value(self, key):
        index = self.hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
                return all_keys

my_hash_table = HashTable()
my_hash_table.set_item('Rahul', 10)
my_hash_table.set_item('Rahul', 10)
print(my_hash_table.keys())
#my_hash_table.print_table()

