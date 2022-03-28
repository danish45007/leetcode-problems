def print_right_triangle(n):
   for i in range(0, n):
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # printing stars
            print("* ",end="")
      
        # ending line after each row
        print("\r")

print(print_right_triangle(6))