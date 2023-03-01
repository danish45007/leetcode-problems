from ArithmeticExpression import ArithmeticExpression
from Operation import Operation

class Expression(ArithmeticExpression):
    def __init__(self,left_number,operation,right_number):
        self.left_number = left_number
        self.right_number = right_number
        self.operation = operation
    
    def eval(self):
        if self.operation == Operation.ADD:
            return self.left_number.eval() + self.right_number.eval()
        elif self.operation == Operation.SUB:
            return self.left_number.eval() - self.right_number.eval()
        elif self.operation == Operation.MUL:
            return self.left_number.eval() * self.right_number.eval()
        elif self.operation == Operation.DIV:
            return self.left_number.eval() / self.right_number.eval()