import my_math
import sys  
import regular_expresions as regex


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
    
    return reduced_form

def print_reduced_form(reduced_form:list):
    """
    Print the reduced form
    """
    print("Reduced form: ", end = "")
    for monomial in reduced_form:
        sign = "+ "
        if monomial[0] < 0: sign = "- "
        elif monomial is reduced_form[0]: sign = ""
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
    print_reduced_form(reduced_form)

    is_equal = True
    for monomial in reduced_form:
        if int(monomial[0]) != 0 or int(monomial[1] != 0):
            is_equal = False
    if is_equal:
        print("Any real number is a solution")
        exit()

    if reduced_form[-1][1] > 0:
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
        print(my_math.second_degree_equation(a, b, c))
    elif reduced_form[-1][1] == 0:
        print("No solution.")
    else:   
        print(f"The solution is:\n{(reduced_form[0][0] * -1) / reduced_form[1][0]}")

    
if __name__=="__main__":
    computor()
