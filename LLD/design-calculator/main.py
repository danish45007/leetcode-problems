from Operation import Operation
from Number import Number
from Expression import Expression

if  __name__ == "__main__":
    # 2 * (3+1)
    two_number = Number(2)
    three_number = Number(3)
    one_number = Number(1)
    
    sub_expression = Expression(three_number,Operation.ADD,one_number)
    parent_expression = Expression(two_number,Operation.MUL,sub_expression)
    print(parent_expression.eval())
