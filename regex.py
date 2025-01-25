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
        temp = temp[pos_end:leng]
    
    return monomials

def read_monomial(string:str):
    """
    obtain the sing, the coefficient and exponent of a monomial
    """
    regexs = [r" ?[+-]? ?", #sign
            r"\d+(\.\d+)?", #coefficient
            r" \* X\^",     #literal
            r"\d+"]         #exponent
    leng:int = len(string)
    parts = list()
    pos_end:int = 0

    for regex in regexs:
        span = re.match(regex, string)
        if span.span()[1] == 0:
            parts.append("+")
        else:  
            pos_end = span.span()[1]
            parts.append(string[0:pos_end])
            string = string[pos_end:leng]       

    return parts
