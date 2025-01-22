import re
import sys

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
    temp = temp[pos_end +1:leng]

print(monomials)
