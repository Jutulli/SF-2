from animal import Animal

class Mammal(Animal):
    def reproduce(self) -> None:
        super().reproduce()
        print("Mammals give bith to live young, and raise them until they can be independant.")

    def __repr__(self) -> str:
        return super().__repr__() + "\nClass: Mammal"