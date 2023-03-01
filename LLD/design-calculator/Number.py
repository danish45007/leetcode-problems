from ArithmeticExpression import ArithmeticExpression

class Number(ArithmeticExpression):
    def __init__(self, number):
        self.number = number
    
    def eval(self):
        return self.number
    
    