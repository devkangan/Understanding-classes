class Person():
    name = "John"  #name and age are shared with all the instances of this class
    age = 40
    languages = []

person1 = Person() #instance of the Person class
person2 = Person() 

print(person1.name)
print(id(person1.name))
print(id(Person.name))

person1.name = "Kriti"
Person.name = "Sai"
print(person1.name)
print(person2.name)
print(person1.name)
print(id(person1.name))
print(id(person2.name))
print(id(Person.name))

#person1 is not Sai it is Krigtgi only while person2.name --> Sai

Person.salary = 34000
print(person1.salary) #salary variable can be accessed from all the instances variables
person1.salary = 54000  #this would create a new instance variable only for "peson1".

person1.languages.append('English')
print(Person.languages)
print(person1.languages)

print(person2.languages) #Since we are adding in the shared list hence all the instance variables will have same list

person1.languages = ['French'] #this is a separate instance variable
person1.languages.append('Japanese')
print(person1.languages)

'''Keep in consideration when creating mutable instance variable'''