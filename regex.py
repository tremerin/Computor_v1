import re
import sys

#expresiones regulares
regex = r" ?[+-]? ?\d+(\.\d+)? X\^\d+"
len:int = len(sys.argv[1])
temp:str
monomios = list()
print(type(monomios))
print("len:", len)
span = re.match(regex, sys.argv[1])
print(span)
if span == None:
    exit()
monomio = sys.argv[1][span.span()[0]:span.span()[1]]
print("monomio:", monomio)
monomios.append(monomio)
#print(re.findall(regex, sys.argv[1]))
if span.span()[1] < len:
    temp = sys.argv[1][span.span()[1]:len-1]
    print(temp)
    span = re.match(regex, temp)
    print(span)