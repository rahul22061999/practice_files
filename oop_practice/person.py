import csv

class Person:
    all_people = []  # List to keep track of all created Person instances

    def __init__(self, name, age, city):
        """
        Constructor method to initialize a Person object.
        :param name: Name of the person
        :param age: Age of the person
        :param city: City where the person lives
        """
        self.__name = name
        self.age = age
        self.city = city
        Person.all_people.append(self)  # Add the new Person instance to the all_people list

    def __repr__(self):
        """
        Representation method to return a string representation of a Person object.
        """
        return f"{self.__class__.__name__}(name='{self.name}', age={self.age}, city='{self.city}')"

    @classmethod
    def load_from_csv(cls, filename):
        """
        Class method to load data from a CSV file and create Person instances.
        :param filename: Name of the CSV file
        """
        with open(filename, 'r') as f:  # Use the provided filename parameter
            reader = csv.DictReader(f)  # Create a CSV reader object
            for row in reader:  # Iterate over each row in the CSV file
                # Create a new Person instance using data from the current row
                cls(
                    name=row['Name'],
                    age=int(row['Age']),
                    city=row['City']
                )
    @property 
    # Read only decorator 
    def name(self):
        return self.__name 
    
    @name.setter
    def name(self, value):
        self.__name = value 

# Example usage:
Person.load_from_csv('person.csv')  # Load data from the CSV file

print(Person.all_people)
