def solve(n):
    # base condition
    if n == 1:
        print(n)
        return
    # hypothesis
    solve(n-1)
    # induction
    print(n)
    

solve(7)

"""
# hypothesis
solve(n) ---> 1,n
solve(n-1) ---> 1,n-1
.
..
...
solve(1) ---> hit my base condition
print() --> induction
"""