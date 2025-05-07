from mammal import Mammal
from pet import Pet
from omnivore import Omnivore

class Parrot(Mammal, Omnivore, Pet):
    def __init__(self, legs=4, tail=1, ears=2):
        self.tail = tail
        self.ears = ears
        super().__init__(legs)

    def __repr__(self) -> str:
        result = Mammal.__repr__(self) + '\nSpecies: Dog'
        result += '\n' + Pet.__repr__(self)

        return result + '\n' + Omnivore.__repr__(self)
    
    def move(self) -> None:
        print("I move by walking and running, sometimes very fast!")

    def sleep(self) -> None:
        print("Dogs are diurnal creatures, prefering to sleep during the night from 9pm to 6am. They also are take naps throughout the day.")

    def reproduce(self) -> None:
        Mammal.reproduce(self)
        print("Dogs typically birth 1-12 puppies, taking care of them until they are independant. They can reproduce once per year generally.")

    def eat(self) -> None:
        Omnivore.eat(self)
        #print("When domesticated, I tend to mainly eat dog food, with occasional treats. I can also eat most vegetables and some fruits.")