import re
from decimal import Decimal


def valid_syntax(string:str):
    """
    Finds and prints syntax errors by underlining the error in red

    Parameters:
    string (str): One of the terms of an equation in text format.

    Return:
    value (bool): Returns true or false if the syntax is correct.
    """
    regexs = {
        r"[^0-9X\*\^\.\+\-\s]"          :   "Invalid character              :",
        r"\s{2,}"                       :   "More than one space together   :",
        r"X{2,}"                        :   "More than one X together       :",
        r"\^{2,}"                       :   "More than one ^ together       :",
        r"[+-]{2,}"                     :   "More than one sign together    :",
        r"\*{2,}"                       :   "More than one * together       :",
        r"\.{2,}"                       :   "More than one . together       :",
        r"X \^"                         :   "Incorrect space                :",
        r"X\^ \d*"                      :   "Incorrect space                :",
        r"X\^\d+\.\d*"                  :   "Decimal exponent               :",
        r"X\s*\^\s{1,}"                 :   "Need a exponent                :",
        r"[+-]\s*\*|[+-]\s*$"           :   "No coefficient                 :",
        r"[+-]\s*[+-]"                  :   "No coefficient                 :",
        r"^\s*\*"                       :   "No coefficient                 :",
        r"\d+\. |\s{1,}\."              :   "Decimal part missing           :",
        r"\d+\.\d+\."                   :   "Invalid expresion              :",
        r"\d+\s*X"                      :   "Need * symbol                  :",
        r"\d+\s{1,}\d+"                 :   "Need sign between monomials    :",
        r"\d+\*|\*X|\d+[+-]"            :   "Need one space                 :",
        r"^\s*$"                        :   "There is no monomial in the term",                 
        r"\^[+-]\d+"                    :   "Sign in the exponent           :"
    }

    valid = True
    for key, value in regexs.items():
        errors = re.findall(key, string)
        if len(errors) > 0:
            corrected = string
            valid = False
            if value == "Invalid character              :":
                for error in errors:
                    corrected = re.sub(error, f"\033[41m{error}\033[0m",corrected)
            else:
                for error in errors:
                    corrected = re.sub(key, f"\033[41m{error}\033[0m",corrected)
            print(f"Error: {value} {corrected}")

    return valid
    

def get_monomials_bonus(string:str):
    """
    Separates and return a member of an equation by monomials
    """
    monomials = list()
    regexs = [r"([+-])",                                #sign
            r"\s*\d+(\.\d+)? \* X\^\d+\s*",             #complete monomial
            r"\s*\d+\s*$",                              #only coefficient
            r"\s*\d+(\.\d+)? \* X\s*$",                 #no exponent
            r"\s*X\^\d+\s*$"]                           #no coefficient

    normalize = [lambda sign, piece: sign + piece,
            lambda sign, piece: sign + " " + piece + " * X^0",
            lambda sign, piece: sign + " " + piece + "^1",
            lambda sign, piece: sign + " " + "1 * " + piece]

    split_string = [string for string in re.split(regexs[0], string) if string]
    if split_string[0] not in ["-", "+"]:
        split_string.insert(0, "+")
    sign = ""
    for piece in split_string:
        for i in range(len(regexs)+1):
            if i == len(regexs):
                print("Error: Bad syntax")
                exit()
            span = re.match(regexs[i], piece)
            if span != None:
                if i == 0:sign = piece
                else:
                    piece = re.sub(r"\s*$", "", re.sub(r"^\s*", "", piece))
                    monomials.append(normalize[i-1](sign, piece))
                break

    return monomials


def read_monomial(string:str):
    """
    Obtain the sing, the coefficient and exponent of a monomial
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
        value.append(Decimal(parts[1]))
    else:
        value.append(Decimal(parts[1]) * -1)
    value.append(int(parts[3]))

    return value


def split_equation_terms(string:str):
    """
    Separate terms of the equation and check the syntax
    """
    regex = r"\s*=\s*" #equal
    #regex = r"=" #equal
    equation_terms = re.split(regex, string)
    if len(equation_terms) > 2:
        print("Error: Bad syntax, two or more \"=\" simbol")
        exit()
    elif len(equation_terms) == 1:
        print("Error: Bad syntax, no \"=\" simbol")
        exit()

    return equation_terms