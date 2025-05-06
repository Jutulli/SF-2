from animal import Animal

class Reptile(Animal):
    def reproduce(self) -> None:
        super().reproduce()
        print("Reptiles produce by laying eggs, typically on land rather than water.")

    def __repr__(self) -> str:
        return super().__repr__() + "\nClass: Reptile"