import math
import sys  
import regex # type: ignore

def second_degree_equation(a:float, b:float, c:float):
    """
    Calculate the discriminant and the solution, if possible, of the quadratic equation.
    """
    dis = (b * b) - (4 * c * a)
    if dis <0:
        print("The solution is not a real number")
    else:
        x1 = (-b - math.sqrt(dis)) / (2 * a)
        print(f"x1: {round(x1, 6)}")
        x2 = (-b + math.sqrt(dis)) / (2 * a)
        print(f"x2: {round(x2, 6)}")

def read_monomials(equation_terms:list):
    """
    Decomposes the text string into monomials
    """
    if len(equation_terms) != 2:
        print("Error: Bad syntax")
        exit()
    first = regex.get_monomials(equation_terms[0])
    second = regex.get_monomials(equation_terms[1])
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
        print(f"{sign}{abs(coefficient)} * X^{monomial[1]} ", end = "")
    print("= 0")

def computor():
    """
    Solves first and second degree equations given as monomials in a text string
    """
    if len(sys.argv) != 2:
        print("Usage: Enter as the only argument the equation expressed in monomials")
        exit()

    monomials = read_monomials(sys.argv[1].split(" ="))

    reduced_form = equation_reduced_form(monomials)

    if len(reduced_form) == 0:
        print("Each real number is a solution")
        exit()

    print_reduced_form(reduced_form)
    print(f"Polynomial degree: {reduced_form[-1][1]}")

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
        print(f"The solution is:\n{(reduced_form[0][0] * -1) / reduced_form[1][0]}")

    
if __name__=="__main__":
    computor()
