import math
import sys  
import regex # type: ignore


def  irreducible_fraction(numerator:float, denominator:float):
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
        irreducible = f"{round(numerator, 6)}/{round(denominator, 6)}"
    return irreducible


def second_degree_equation(a:float, b:float, c:float):
    """
    Calculate the discriminant and the solution, if possible, of the quadratic equation.
    """
    dis = (b * b) - (4 * c * a)
    if dis <0:
        print("The solution is not a real number")
    else:
        numerator = -b - math.sqrt(dis)
        denominator = 2 * a
        x1 = x2 = ""
        if numerator % denominator == 0:
            x1 = round(numerator, 6), round(denominator, 6)
        else:
            x1 = irreducible_fraction(round(numerator, 6), round(denominator, 6))
        print(f"x1: {x1}")
        numerator = -b + math.sqrt(dis)
        if numerator % denominator == 0:
            x2 = round(numerator, 6), round(denominator, 6)
        else:
            x2 = irreducible_fraction(round(numerator, 6), round(denominator, 6))
        print(f"x2: {x2}")


def read_monomials(string:str):
    """
    Decomposes the text string into monomials
    """
    equation_terms = regex.split_equation_terms(string)
    valid_first = regex.valid_syntax(equation_terms[0])
    valid_second = regex.valid_syntax(equation_terms[1])
    if not valid_first or not valid_second:
        exit()
    first = regex.get_monomials_bonus(equation_terms[0])
    second = regex.get_monomials_bonus(equation_terms[1])
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
    else:   
        print(f"The solution is:\nx = {irreducible_fraction((reduced_form[0][0] * -1), reduced_form[1][0])}")

    
if __name__=="__main__":
    computor()
