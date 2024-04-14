class Person():
    name = "Kriti"
    age = 38

    def introduction(self):
        '''
        Instance method: Function defined inside the class called on each instance.
        '''    
        return f"My name is {name} and age is {age}"
    
    def selfintroduction(self):
        return f"My name is {self.name} and age is {self.age}"
    
    def change_name(self, name):
        self.name = name #Person1.name = name
        self.salary = 40000
        self.selfintroduction()

person1 = Person()
#print(person1.introduction()) #this will raise an error since python looks for name variable locally.
#print(person1.selfintroduction()) #When we call a method, the first argument is actually the instance on which the method is called.
#print(Person.introduction(person1)) #self is nothing but person1 itself.

print(person1.change_name('Stuti'))
Person.change_name(person1, 'Stuti')  #Line 24  is for Line 23

