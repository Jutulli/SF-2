from bird import Bird
from pet import Pet
from omnivore import Omnivore

class Parrot(Bird, Omnivore, Pet):
    def __init__(self, legs=4, wings=2, Color = "Yellow"):
        self.Color = Color
        super().__init__(legs=legs, wings=wings)

    def __repr__(self) -> str:
        result = Bird.__repr__(self) + '\nSpecies: Parrot'
        result += '\n' + Pet.__repr__(self)

        return result + '\n' + Omnivore.__repr__(self)
    
    def move(self) -> None:
        print('I can move in various ways. I can fly, walk, climb and even \
use a unique method called "beakiation" to traverse narrow branches.')

    def sleep(self) -> None:
        print("Parrots sleep around 10 to 12 hours each night, often tucked their wings. \
They may also take naps during the day.")

    def reproduce(self) -> None:
        Bird.reproduce(self)
        print("Parrots often take a few days to lay a full clutch of eggs. \
This can be as many as three to four eggs.")

    def eat(self) -> None:
        Omnivore.eat(self)
        print("I eat both plant and animal matter. My natural diet includes \
a variety of food like seeds , nuts, fruits, vegetables, flowers, bud and insects.")
        

p1 = Parrot()
print(p1)
p1.move()
p1.sleep()
p1.reproduce()
p1.eat()