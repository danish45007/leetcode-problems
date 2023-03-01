from abc import ABC, abstractclassmethod

class ArithmeticExpression(ABC):
    
    @abstractclassmethod
    def eval(self):
        pass
        