class Person():

    __hash__ = None #To make object unhashable in case if eq is not used
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person('{self.name}','{self.age}')"
    
    def __str__(self) -> str:
        return f"{self.name}"
    # def __eq__(self, other):
    #     return self.name == other.name and self.age == other.age

person1 = Person('Dia', 43)
person2 = Person('Dia', 43)

print(person1) #Person object and address
string1 = "a"
string2 = "b"
print(string1 + string2)
print(string1.__add__(string2)) #python does this under hood evrytime comparing or len or + is greater than, is less than
print(repr(person1))
print(person1.__repr__())
print(person1) #repr is fallback if you don't specify the str method

person_string = str(person1) #str method converts the object to a string
print(person_string) 
print("----")
print(person1.__str__())
print(person1 == person2) #because calling eq method

print(hash(person1))