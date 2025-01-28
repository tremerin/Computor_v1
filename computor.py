import math #raiz cuadrada
import sys  #pasar argumentos al programa
import regex

def second_degree_equation(a:float, b:float, c:float):
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
    print(equation_terms)
    print("Error =")
    exit()

first = regex.get_monomials(equation_terms[0])
#print(f"{first}")
second = regex.get_monomials(equation_terms[1])
#print(f"{second}")
monomials = list()

for monomial in first:
    monomials.append(regex.read_monomial(monomial))
for monomial in second:
    new_monomial = regex.read_monomial(monomial)
    new_monomial[0] = new_monomial[0] * -1
    monomials.append(new_monomial)

#print(monomials)

#crear reduced_form
reduced_form = list()

for monomial in monomials:
    new_exponent = True
    for mono in reduced_form:
        if monomial[1] == mono[1]:
            mono[0] += monomial[0]
            new_exponent = False
    if new_exponent:
        reduced_form.append(monomial)

#ordenar reduced_form
#print(reduced_form)


for i in range(len(reduced_form)):
    min_exp = reduced_form[i][1]
    for j in range(len(reduced_form)):
        if reduced_form[j][1] > min_exp:
            min_exp = reduced_form[j][1]
            temp = reduced_form[i]
            reduced_form[i] = reduced_form[j]
            reduced_form[j] = temp


#print(reduced_form)
print("Reduced form: ", end = "")
for monomial in reduced_form:
    sign = "+ "
    if monomial[0] < 0: sign = "- "
    coefficient = monomial[0]
    if monomial[0] % 1 == 0: coefficient = int(monomial[0])
    print(f"{sign}{abs(coefficient)} * X^{monomial[1]} ", end = "")
print("= 0")

print(f"Polynomial degree: {reduced_form[-1][1]}")
#comprobar max_expo
if reduced_form[-1][1] > 2:
    print("The polynomial degree is strictly greater than 2, I can't solve.")
    exit()
elif reduced_form[-1][1] == 2:
    second_degree_equation(reduced_form[2][0], reduced_form[1][0], reduced_form[0][0])
else:   
    print(f"The solution is:\n{(reduced_form[0][0] * -1) / reduced_form[1][0]}")