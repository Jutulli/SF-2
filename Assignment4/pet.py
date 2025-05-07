from abc import ABCMeta

class Pet(object, metaclass = ABCMeta):
    def __init__(self, legs=0):
        self.legs = legs

    def pet(self) -> None:
        return "You can pet this animal!"
    
    def __repr__(self) -> str:
        return "This animal is a pet."