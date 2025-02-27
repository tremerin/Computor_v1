import math
import sys  
import regular_expresions as regex


def irreducible_fraction(numerator:float, denominator:float, precision:int = 6):
    """
    Claculate the irreducible form of a fraction
    """
    irreducible:str = ""

    if type(numerator) == float or type(denominator) == float:
        return f"{numerator}/{denominator}"
    
    divisor = math.gcd(numerator, denominator)

    if numerator % divisor == 0 and denominator % divisor == 0:
        if denominator/divisor == 1:
            irreducible = f"{numerator/divisor}"
        else:
            irreducible = f"{int(numerator/divisor)}/{int(denominator/divisor)}"
    else:
        irreducible = f"{round(numerator, precision)}/{round(denominator, precision)}"
    return irreducible


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
    
    guess = number / 2
    while abs(guess**2 - number) > precision:
        guess = (guess + number / guess) / 2
    
    return guess


def second_degree_equation(a:float, b:float, c:float):
    """
    Calculate the discriminant and the print the solutions, if possible, of the quadratic equation.

    Parameters:
    a (float): The coefficient of x^2.
    b (float): The coefficient of x.
    c (float): The constant term.
    """
    dis = (b * b) - (4 * c * a)
    if dis <0:
        print("The solution is not a real number")
    else:
        numerator = -b - square_root(dis)
        denominator = 2 * a
        x1 = x2 = ""
        if numerator % denominator == 0:
            x1 = round(numerator, 6), round(denominator, 6)
        else:
            x1 = irreducible_fraction(round(numerator, 6), round(denominator, 6))
        print(f"x1: {x1}")
        numerator = -b + square_root(dis)
        if numerator % denominator == 0:
            x2 = round(numerator, 6), round(denominator, 6)
        else:
            x2 = irreducible_fraction(round(numerator, 6), round(denominator, 6))
        print(f"x2: {x2}")


def read_monomials(string:str):
    """
    Decomposes the text string into monomials.

    Parameters:
    string (str): Equation in text format.

    Returns:
    list: Returns a list of monomials
    """
    equation_terms = regex.split_equation_terms(string)
    valid_first = regex.valid_syntax(equation_terms[0])
    valid_second = regex.valid_syntax(equation_terms[1])
    if not valid_first or not valid_second:
        exit()
    first = regex.get_monomials_bonus(equation_terms[0])
    second = regex.get_monomials_bonus(equation_terms[1])
    if len(first) == 0 or len(second) == 0:
        print("Error: Bad syntax")
        exit()
    monomials = list()

    for monomial in first:
        monomials.append(regex.read_monomial(monomial))
    for monomial in second:
        new_monomial = regex.read_monomial(monomial)
        new_monomial[0] = new_monomial[0] * -1
        monomials.append(new_monomial)

    return monomials


def equation_reduced_form(monomials:list):
    """
    Operate the monomials of both terms to obtain the reduced form of the equation
    """
    reduced_form = list()

    for monomial in monomials:
        new_exponent = True
        for mono in reduced_form:
            if monomial[1] == mono[1]:
                mono[0] += monomial[0]
                new_exponent = False
        if new_exponent:
            reduced_form.append(monomial)

    for i in range(len(reduced_form)):
        min_exp = reduced_form[i][1]
        for j in range(len(reduced_form)):
            if reduced_form[j][1] > min_exp:
                min_exp = reduced_form[j][1]
                temp = reduced_form[i]
                reduced_form[i] = reduced_form[j]
                reduced_form[j] = temp

    for monomial in reduced_form:
        if monomial[0] == 0:
            reduced_form.remove(monomial)
    
    return reduced_form


def print_reduced_form(reduced_form:list):
    """
    Print the reduced form
    """
    print("Reduced form: ", end = "")
    for monomial in reduced_form:
        sign = "+ "
        if monomial[0] < 0: sign = "- "
        coefficient = monomial[0]
        if monomial[0] % 1 == 0: coefficient = int(monomial[0])
        print(f"{sign}{abs(coefficient)} * X^{monomial[1]} ", end = "") #

    print("= 0")


def max_decimal_len(nums:list):
    """
    Calculate the number with the most decimal places in a list
    """
    max_decimals: int = 0
    for num in nums:
        i = 0
        while num % 1 != 0:
            num *= 10
            i += 1
        if i > max_decimals: max_decimals = i
    return max_decimals


def solve_decimals(reduced_form:list):
    """
    Remove decimals from coefficients
    """
    solved_form = reduced_form
    coefficients = [num[0] for num in reduced_form]
    multi = pow(10, max_decimal_len(coefficients))
    for monomial in solved_form:
        monomial[0] = int(monomial[0] * multi)
    return solved_form


def computor():
    """
    Solves first and second degree equations given as monomials in a text string
    """
    if len(sys.argv) != 2:
        print("Usage: Enter as the only argument the equation expressed in monomials")
        exit()

    monomials = read_monomials(sys.argv[1])
    reduced_form = equation_reduced_form(monomials)

    if len(reduced_form) == 0:
        print("Each real number is a solution")
        exit()

    print_reduced_form(reduced_form)
    print(f"Polynomial degree: {reduced_form[-1][1]}")

    reduced_form = solve_decimals(reduced_form)
    if reduced_form[-1][1] > 2:
        print("The polynomial degree is strictly greater than 2, I can't solve.")
        exit()
    elif reduced_form[-1][1] == 2:
        a = b = c = 0
        for monomial in reduced_form:
            if monomial[1] == 2: a = monomial[0]
            elif monomial[1] == 1: b = monomial[0]
            elif monomial[1] == 0: c = monomial[0]
        second_degree_equation(a, b, c)
    elif reduced_form[-1][1] == 0:
        print("Invalid expresion")
    else:   
        print(f"The solution is:\nx = {irreducible_fraction((reduced_form[0][0] * -1), reduced_form[1][0])}")

    
if __name__=="__main__":
    computor()
