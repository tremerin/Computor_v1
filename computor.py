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
argument_split = sys.argv[1].split(" =")
if len(argument_split) != 2:
    print("Error =")
    exit()

first = regex.get_monomials(argument_split[0])
print(f"-{first}-")
second = regex.get_monomials(argument_split[1])
print(f"-{second}-")

max_expo = 0
