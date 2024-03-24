class car:
    def __init__(self, color, make, model):
        self.color = color
        self.make = make 
        self.model = model 
    
    def drive(self):
        return 'The {} {} {} is driving'.format(self.color, self.make,self.model)
    
car1 = car("Red", "Toyota", "Corolla")
car2 = car("Blue", "Honda", "Civic")

print(car2.drive())