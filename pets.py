class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        raise NotImplementedError("Sub Class implement")

class Cat(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)

    def talk(self):
        return "miaow"

class Dog(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)

    def talk(self):
        return "guk guk"

def Main():
    pets = [Cat("jess", 3),
            Dog("jack",4),
            Cat("fred", 7),
            Pet("thePet", 4)]

    for pet in pets:
        print("name: "+pet.name+", age: "+str(pet.age)+" "+pet.talk())

if __name__ == '__main__':
    Main()

