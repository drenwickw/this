class Dog(object):

    # Class attribute
    species = 'mammal'

    # Initializer
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    # instance method
    def description(self):
        return "{} is {} years old and is {}".format(self.name, self.age, self.sex)

    #instance method
    def speak(self, sound):
        return "{} says {}". format(self.name, sound)

# instantiate the dog object
mikey = Dog("Mikey", 6, "male")
lucy = Dog("Lucy", 2, "female")

#call the methods
print (mikey.description())
print (lucy.description(), lucy.speak(input("what should lucy say? ")))
