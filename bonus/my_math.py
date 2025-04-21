def gcd(a:int , b:int):
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


def irreducible_fraction(numerator:float, denominator:float, precision:int = 6, opt = False):
    """
    Returns the irreducible fraction of the given numerator and denominator.
    
    If either the numerator or denominator is a float, the function returns a string 
    representation of the fraction without reduction. Otherwise, it simplifies the fraction 
    using the greatest common divisor (GCD).

    Parameters:
        numerator (float): The numerator of the fraction.
        denominator (float): The denominator of the fraction.
        precision (int, optional): The number of decimal places to round floats. Default is 6.

    Returns:
        str: The irreducible fraction as a string.
    """
    irreducible:str = ""

    #if type(numerator) == float or type(denominator) == float:
    #    return f"{numerator}/{denominator}"
    
    divisor = gcd(numerator, denominator)
    i = ""
    if opt == True:
        i = "i"

    if numerator % divisor == 0 and denominator % divisor == 0:
        if denominator/divisor == 1:
            irreducible = f"{numerator/divisor}{i}"
        else:
            irreducible = f"{int(numerator/divisor)}{i}/{int(denominator/divisor)}"
    else:
        irreducible = f"{round(numerator, precision)}{i}/{round(denominator, precision)}"
    return irreducible


def second_degree_equation(a:float, b:float, c:float):
    """
    Solves a second-degree (quadratic) equation of the form ax^2 + bx + c = 0.

    The function calculates the discriminant (Δ) to determine the nature of the solutions:
      - If Δ < 0 → The equation has no real solution.
      - If Δ = 0 → The equation has one real solution.
      - If Δ > 0 → The equation has two distinct real solutions.

    The roots are returned in their simplest form, either as a rounded number or an irreducible fraction.

    Parameters:
        a (float): Coefficient of x^2 (must be nonzero).
        b (float): Coefficient of x.
        c (float): Constant term.

    Returns:
        str: A formatted string displaying the solution(s). If no real solution exists, 
             the function returns a message indicating this.
    """
    dis = (b * b) - (4 * c * a)
    if dis <0:
        text= "Discriminant is strictly negative, the two complex solutions are:"
        x1 =f"{irreducible_fraction(-b, 2*a)} + {irreducible_fraction(round(square_root(dis*-1), 6), 2*a, 6, True)}"
        x2 =f"{irreducible_fraction(-b, 2*a)} - {irreducible_fraction(round(square_root(dis*-1), 6), 2*a, 6, True)}"
        return f"{text}\n{x1}\n{x2}"
    elif dis == 0:
        x = -b / (2 * a)
        return f"x: {x}"
    else:
        numerator = -b - square_root(dis)
        denominator = 2 * a
        x1 = x2 = ""
        if numerator % denominator == 0:
            x1 = round(numerator, 6), round(denominator, 6)
        else:
            x1 = irreducible_fraction(round(numerator, 6), round(denominator, 6))
        numerator = -b + square_root(dis)
        if numerator % denominator == 0:
            x2 = round(numerator, 6), round(denominator, 6)
        else:
            x2 = irreducible_fraction(round(numerator, 6), round(denominator, 6))
        return f"x1: {x1}\nx2: {x2}"