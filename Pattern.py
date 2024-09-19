def number_pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")
        
        # Print the ascending part of the numbers
        for j in range(1, i + 1):
            print(j, end="")
        
        # Print the descending part of the numbers
        for j in range(i - 1, 0, -1):
            print(j, end="")
        
        # Move to the next line
        print()

# Example usage
n = 5
number_pyramid(n)
