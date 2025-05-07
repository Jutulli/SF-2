from heterotroph import Heterotroph

class Carnivor(Heterotroph):
    def eat(self) -> None:
        super().eat()
        print("I eat meat.")

    def __repr__(self) -> str:
        return super().__repr__() + '\nThis organism is a carnivore. It feeds on other animals, and its physical features facilitate hunting.'