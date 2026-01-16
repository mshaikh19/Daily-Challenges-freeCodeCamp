# Integer Hypotenuse
# Given two positive integers representing the lengths for the two legs (the two short sides) of a right triangle, determine whether the hypotenuse is an integer.

# The length of the hypotenuse is calculated by adding the squares of the two leg lengths together and then taking the square root of that total (a2 + b2 = c2).


def is_integer_hypotenuse(a, b):
    """
    Firstly we need to calculate the hypotenuse
        c**2 = (a**2) (b**2)
    and then we need to check square root of the hypotenuse
        c = (c**2)**0.5
    then we need to check if the number is an integer by mod 1
        c % 1 == 0
    """

    if(((a**2) + (b**2))**0.5) % 1 == 0 :
        return True
    else:
        return False

print(is_integer_hypotenuse(3, 4))
print(is_integer_hypotenuse(2, 3))
print(is_integer_hypotenuse(5, 12))
print(is_integer_hypotenuse(10, 10))
print(is_integer_hypotenuse(780, 1040))
print(is_integer_hypotenuse(250, 333))