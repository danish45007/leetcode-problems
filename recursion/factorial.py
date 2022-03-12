def factorial(n):
    # base condition (minimum valid input)
    res = 0
    if n == 0:
        return 1
    # hypothesis
    res += n*factorial(n-1)
    # induction 
    return res

print(factorial(10))
    