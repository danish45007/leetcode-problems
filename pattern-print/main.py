'''
*
* *
* * *
* * * *
* * * * *
'''
def pattern1(n):
    for row in range(1,n+1):
        for col in range(1,row+1):
            print('* ',end='')
        print('\n')


'''
* * *
* * *
* * *

'''

def pattern2(n):
    for row in range(1,n+1):
        for col in range(n):
            print('* ',end='')
        print('\n')

'''
* * * *
* * *
* *
*
'''

def pattern3(n):
    for row in range(n):
        for col in range(n-row):
            print('* ', end='')
        print('\n')

'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

def pattern4(n):
    for row in range(1,n+1):
        for col in range(1,row+1):
            print(f'{col} ',end='')
        print('\n')
        
'''
*
* *
* * *
* * * *
* * *
* *
*
'''

def pattern5(n):
    for row in range(1,2*n):
        if row > n:
            total_col = 2*n-row
        else:
            total_col = row
        for col in range(1,total_col+1):
            print('* ',end='')
        print('\n')        


'''
      *
     * *
    * *	*
     * *
      *

'''

def pattern6(n):
    for row in range(1,2*n):
        if row > n:
            total_col = 2*n-row
        else:
            total_col = row
        space = abs(n-total_col)
        for s in range(space+1):
            print(' ',end='')
        for col in range(1,total_col+1):
            print('* ',end='')
        print('\n')

'''
      1
    2 1 2
  3 2 1 2 3

'''

def pattern7(n):
    for row in range(1,n+1):
        # first section [row,1]
        spaces = n - row
        for s in range(spaces):
            print('  ',end='')
        for c1 in range(row,0,-1):
            print(f'{c1} ',end='')
        # section section [2,row]
        for c2 in range(2,row+1):
            print(f'{c2} ',end='')
        print('\n')


'''

      1
    2 1 2
  3 2 1 2 3
    2 1 2
      1 
'''

def pattern8(n):
    for row in range(1,2*n+1):
        if row > n:
            total_col = 2*n - row
        else:
            total_col = row
        
        spaces = abs(n-row)
        for space in range(spaces):
            print('  ',end='')
        for c1 in range(total_col,0,-1):
            print(f'{c1} ',end='')
        for c2 in range(2,total_col+1):
            print(f'{c2} ',end='')
        print('\n')

'''
 4 4 4 4 4 4 4
 4 3 3 3 3 3 4
 4 3 2 2 2 3 4
 4 3 2 1 2 3 4
 4 3 2 2 2 3 4
 4 3 3 3 3 3 4
 4 4 4 4 4 4 4
 '''
 
def pattern9(n):
    actual_n = n
    n = 2*n
    for row in range(n+1):
        for col in range(n+1):
            val_at_each_index = actual_n - min(row,n-row,col,n-col)
            print(f'{val_at_each_index} ',end='')
        print('\n')
     

if  __name__ == "__main__":
    pattern9(4)