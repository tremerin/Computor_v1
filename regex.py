import re

def get_monomials(string:str):
    """
    separates and return a member of an equation by monomials
    """
    regex = r" ?[+-]? ?\d+(\.\d+)? \* X\^\d+"
    leng:int = len(string)
    monomials = list()
    pos_end:int = 0

    while len(string) > 0:
        span = re.match(regex, string)
        if span == None:
                print("Error: Bad Syntax")
                exit()
        pos_end = span.span()[1]
        monomials.append(string[span.span()[0]:pos_end])
        string = string[pos_end:leng]
    
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
    value = list()
    pos_end:int = 0

    for regex in regexs:
        span = re.match(regex, string)
        if span.span()[1] == 0:
            parts.append("+")
        else:  
            pos_end = span.span()[1]
            parts.append(string[0:pos_end])
            string = string[pos_end:leng]

    if "-" not in parts[0]:
        value.append(float(parts[1]))
    else:
        value.append(float(parts[1]) * -1)
    value.append(int(parts[3]))

    return value
