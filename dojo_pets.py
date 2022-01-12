class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()
        return self
        # print("walk")
    
    def feed(self):
        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}!")
            self.pet.eat()
        else:
            print("Out of pet food!")
        return self
        # print("feed")

    def bathe(self):
        self.pet.noise()
        # print("bathe")

class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 50
        self.energy = 100
        self.noise = noise
    
    def sleep (self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        self.energy -= 15
        return self

    def noise(self):
        print(self.noise)

my_treats = ['Scooby Snacks', 'Milk Bones', 'Bacon Strips']
my_pet_food = ['dry food', 'wet food']

cooper = Pet("Cooper", "dog",['sits', 'roll over'], "bark")

cher = Ninja("Cher", "Lafferty", cooper, my_treats,my_pet_food)
cher.feed()
cher.feed()
cher.feed()
