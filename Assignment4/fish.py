from animal import Animal

class Fish(Animal):
    def reproduce(self) -> None:
        super().reproduce()
        print("Fish reproduction varies largely, some give birth to live young while others lay eggs.")

    def __repr__(self) -> str:
        return super().__repr__() + "\nClass: Fish"