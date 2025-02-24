def calculate_gcd(a:int , b:int):
    """
    This function calculates the Greatest Common Divisor (GCD) of two numbers using the Euclidean algorithm.
    The Euclidean algorithm works by repeatedly applying the rule:

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The Greatest Common Divisor of a and b.
    """
    while b != 0:
        a, b = b, a % b
    
    return a


def square_root(number, precision = 0.00001):
    """
    This function calculates the square root of a given number using Newton's method (also known as the Newton-Raphson method).
    The method iteratively improves the guess of the square root until the difference between the square of the guess and the
    number is smaller than the specified precision.

    Parameters:
    number (float): The number to find the square root of.
    precision (float): The precision level to stop the iteration when the difference is smaller than this value. Default is 0.00001.

    Returns:
    float: The square root of the given number.
    If the number is negative, returns an error message.
    """
    if number < 0:
        return "Error: Cannot calculate the square root of a negative number"
    
    guess = number / 2.0
    while abs(guess**2 - number) > precision:
        guess = (guess + number / guess) / 2
    
    return guess
