from person import Person 
class Phone(Person):  # Inherit from the Person class
    
    def __init__(self, name:str, age:float, city:str, broken_phone=0):
        super().__init__(name, age, city)  # Call the parent class constructor

        assert broken_phone >= 0, f"broken phone {broken_phone} is not greater than or equal to 0"

        # Assign to self object 
        self.broken_phone = broken_phone