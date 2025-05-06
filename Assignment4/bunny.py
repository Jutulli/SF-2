from mammal import Mammal
from pet import Pet
from herbivor import Herbivore

class Bunny(Mammal, Herbivore, Pet):
    def __init__(self, legs=4, ears = 2):
        super().__init__(legs)
        self.ears = ears

    def __repr__(self) -> str:
        result = Mammal.__repr__(self) + '\nSpecies: Bunny' #kingdom, class, species
        result += '\n' + Pet.__repr__(self) #pet info

        return result + '\n' + Herbivore.__repr__(self) #herbivore info
    
    def move(self) -> None:
        print("I move by hopping and I can see behind me...")

    def sleep(self) -> None:
        print("Bunnies are noctural animals, typically sleep around 12 to 14 hours a in short, intermitten periods")

    def reproduce(self) -> None:
        Mammal.reproduce(self)
        print("Bunnies can produce multiple litters per year, potentially having 3-8 kits per litter.")

    def eat(self) -> None:
        Herbivore.eat(self)
        print("I mostly eat fresh hay and grass, with some leafy greens and a few pellets. I should only be given fruit and root vegetables, like carrots, as an occasional treat.")

b1 = Bunny()
print(b1)
b1.eat()
b1.move()
b1.sleep()
b1.reproduce()
b1.pet()