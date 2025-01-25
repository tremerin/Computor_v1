import math #raiz cuadrada
import sys  #pasar argumentos al programa
import regex

#formula ecuación
if len(sys.argv) == 4:
    a:float = float(sys.argv[1])
    b:float = float(sys.argv[2])
    c:float = float(sys.argv[3])
    print(f"a:{a}, b:{b}, c:{c}")
    #calcular discriminante positivio
    dis = (b * b) - (4 * c * a)
    if dis <0:
        print("No tiene solucion real")
    else:
        #calcular soluciones
        x1 = (-b + math.sqrt(dis)) / (2 * a)
        print(f"x1: {x1}")
        x2 = (-b - math.sqrt(dis)) / (2 * a)
        print(f"x2: {x2}")


#computor 
equation_terms = sys.argv[1].split(" =")
if len(equation_terms) != 2:
    print("Error =")
    exit()

first = regex.get_monomials(equation_terms[0])
print(f"{first}")
second = regex.get_monomials(equation_terms[1])
print(f"{second}")
monomials = list()

for monomial in first:
    monomials.append(regex.read_monomial(monomial))
for monomial in second:
    new_monomial = regex.read_monomial(monomial)
    new_monomial[0] = new_monomial[0] * -1
    monomials.append(new_monomial)

print(monomials)

reduced_form = list()

for monomial in monomials:
    new_exponent = True
    for mono in reduced_form:
        if monomial[1] == mono[1]:
            mono[0] += monomial[0]
            new_exponent = False
    if new_exponent:
        reduced_form.append(monomial)

print(reduced_form)
max_expo = 0
