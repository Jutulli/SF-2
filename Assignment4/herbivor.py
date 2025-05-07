from heterotroph import Heterotroph

class Herbivore(Heterotroph):
    def eat(self) -> None:
        super().eat()
        print("I eat plants.")

    def __repr__(self) -> str:
        return super().__repr__() + '\nThis organism is a herbivor it feeds on plant \
matter and its physiology facilitates food search '