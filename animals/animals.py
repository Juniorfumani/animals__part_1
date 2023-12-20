class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} eats"

    def sound(self):
        return "sound..."


class Dog(Animal):
    def __init__(self, name="Rax"):
        super().__init__(name)

    def sound(self):
        return "Bark"


class Cat(Animal):
    def __init__(self, name="Stormy"):
        super().__init__(name)

    def sound(self):
        return "Meow"


class Home:
    def __init__(self):
        self.pets_at_home = []

    def adopt_pet(self, new_pet):
        if isinstance(new_pet, Animal):
            if new_pet in self.pets_at_home:
                raise ValueError(
                    "You can not adopt the same pet twice, this pet is already adopted"
                )
            self.pets_at_home.append(new_pet)
            return len(self.pets_at_home)
        else:
            raise ValueError("Invalid pet type. You can only adopt an Animal")

    def make_all_sounds(self):
        all_sounds = [pet.sound() for pet in self.pets_at_home]
        return all_sounds


if __name__ == "__main__":
    dog1 = Dog()
    dog2 = Dog("Simba")

    print(dog1.eat())
    print(dog1.sound())

    print(dog2.eat())
    print(dog2.sound())

    cat1 = Cat()
    cat2 = Cat("Simba")

    print(cat1.eat())
    print(cat1.sound())

    print(cat2.eat())
    print(cat2.sound())

    home = Home()
    dog1 = Dog("Tiger")
    dog2 = Dog("Whiskers")
    cat = Cat("Whiskers")

    print(home.make_all_sounds())

    print("Number of pets adopted:", home.adopt_pet(dog1))
    print(home.make_all_sounds())

    print("Number of pets adopted:", home.adopt_pet(cat))
    print(home.make_all_sounds())
