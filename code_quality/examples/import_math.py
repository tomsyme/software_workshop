"Finding closest square number to my input"

import math

def closest_square(n):
    "Find the square root of the input number"
    root = math.sqrt(n)

    # Find the nearest integers to the square root
    lower = math.floor(root)
    upper = math.ceil(root)

    # Calculate the square of these integers
    lower_square = lower ** 2
    upper_square = upper ** 2

    # Determine which square is closer to the input number
    if abs(n - lower_square) < abs(n - upper_square):
        return lower_square

    return upper_square

# Example usage
number = int(input("Enter a number: "))
print(f"The closest square number to {number} is {closest_square(number)}")
print(f"The square root of {closest_square(number)} is {abs(math.sqrt(closest_square(number)))}")
