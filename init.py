class Person():

    language = "English"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_language(cls, language):
        cls.language = language

    @classmethod
    def from_list(cls, list_data):
        name, age = list_data
        return cls(name,age)
    
    @staticmethod
    def check_age(age):
        return age > 30

person1 = Person('John', 40)
print(person1.name) 
person2 = Person('David', 45)
print(person2.name) 
Person.change_language('Jap')
print(person1.language)
person1.change_language('Fr')
print(person1.language)
print(Person.language)
person_data = ['Stuti', 45]
person3 = Person.from_list(person_data)
print(person3.name)
print(Person.check_age(45))
