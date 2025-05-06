from abc import ABCMeta

class Heterotroph(object, metaclass = ABCMeta):
    def __init__(self, legs = 0, fins = 0, wings = 0):
        self.legs = legs
        self.fins = fins
        self.wings = wings

    def eat(self) -> None:
        print("I eat other organisms instead of generating my own food")
    
    def __repr__(self) -> str:
        return "This organism is a heterorph It is unable to product it's own food "