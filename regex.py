import re


def get_monomials(string:str):
    """
    separates and return a member of an equation by monomials
    """
    regex = r" ?[+-]? ?\d+(\.\d+)? \* X\^\d+"
    leng:int = len(string)
    temp:str = string
    monomials = list()
    pos_end:int = 0

    while len(temp) > 0:
        span = re.match(regex, temp)
        if span == None:
                print("Error: sintaxis")
                exit()
        pos_end = span.span()[1]
        monomials.append(temp[span.span()[0]:pos_end])
        #print(monomials[-1])
        temp = temp[pos_end:leng]
    
    return monomials

def read_monomial(string:str):
    """
    obtain the coefficient and exponent of a monomial
    """
    sign        = r" ?[-+]? ?"
    coefficient = r"\d+(\.\d+)"
    literal     = r" \* X\^"
    exponent    = r"\d+"
    span = re.match(sign, string)
    pass


#signo, coeficiente, literal, exponente // primer termino = segundo termino

"""
#expresiones regulares
if len(sys.argv) != 2:
    print("Error: número de argumentos")
    exit()
regex = r" ?[+-]? ?\d+(\.\d+)? \* X\^\d+"
leng:int = len(sys.argv[1])
temp:str = sys.argv[1]
monomials = list()
pos_end:int = 0

while len(temp) > 0:
    span = re.match(regex, temp)
    if span == None:
            print("Error: sintaxis")
            exit()
    pos_end = span.span()[1]
    monomials.append(temp[span.span()[0]:pos_end])
    print(monomials[-1])
    temp = temp[pos_end:leng]
    print(temp)

print(monomials)
"""