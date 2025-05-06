from abc import ABCMeta, abstractmethod

class Animal(object, metaclass = ABCMeta):
    def __init__(self, legs = 0, fins = 0):
        self.legs = legs
        self.fins = fins
    
    @abstractmethod
    def move(self) -> None:
        pass
    
    @abstractmethod
    def sleep(self) -> None:
        pass

    @abstractmethod
    def eat(self) -> None:
        pass

    def reproduce(self) -> str:
        print('Members of this kingdom repdocude by finding a mate of the same species')

    def __repr__(self) -> str:
        return "Kingdom: Animalia"
    
