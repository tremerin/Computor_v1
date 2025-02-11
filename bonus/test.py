import re
import sys
import math

print("test")
"""
regex = r"([+-])" 
if len(sys.argv) == 2:
    #list comprehension
    split_string = [string for string in re.split(regex, sys.argv[1]) if string]
    if split_string[0] not in ["-", "+"]: 
        split_string.insert(0, "+")
    print(split_string)


valid = r"\s*\d+(\.\d+)? \* X(?:\^\d+\s*$|\s*$)"
valid_n = r"\s*\d+\s*$"
valid2 = r"(?:\s*\d+(\.\d+)? \* X(?:\^\d+\s*$|\s*$)|\s*\d+\s*$|\s*\d+(\.\d+)? \* X \d+\s*$|\s*X\^\d+\s*$)"
for string in split_string:
    span = re.match(valid2, string)
    if span == None:
        print(f"{string}: false")
    else:
        print(f"{string}: true")
"""
  
def get_monomial_bonus(string:str):
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
                print("Error: bat syntax:", piece)
                exit()
            span = re.match(regexs[i], piece)
            if span != None:
                if i == 0:sign = piece
                else:
                    piece = re.sub(r"\s*$", "", re.sub(r"^\s*", "", piece))
                    monomials.append(normalize[i-1](sign, piece))
                break

    return monomials


#print("--- get monomials ---")
#print(get_monomial_bonus(sys.argv[1]))

#lcm (minimo comun multiplo)
def list_lcm(nums:list):
    """
    Gets the least common multiple of a list of numbers
    """
    nums = list(set(nums))
    min_multiplo = nums[0]
    if len(nums) == 1:
        return min_multiplo
    for i in range(len(nums) -1):
        while True:
            multiplo = max(min_multiplo, nums[i + 1])
            if multiplo % nums[i] == 0 and multiplo % nums[i + 1] == 0:
                min_multiplo = multiplo
                break
            else:
                min_multiplo += 1
        
    return min_multiplo


#gcd (maximo comun divisor)
def list_gcd(nums:list):
    """
    Gets the greatest common factor of a list of numbers
    """
    max_div = nums[0]
    for num in nums[1:]:
        print("mcd: ",max_div)
        max_div = math.gcd(max_div, num)
    return(num)

#nums = [12, 36, 42, 51, 24]
#print(f"mcm y mcd de: {nums}")
#print(list_lcm(nums))
#print(list_gcd(nums))

"""
string = "Hola mundo!"
regex = r" {2,}"
regex2 = r"o" 
errors = re.findall(regex2, sys.argv[1])
print(errors)
print(len(errors))
"""

print("-- highlighter --")
normal = "hola mundo mundo inmundo mundo!"
palabra = "mundo"
regex = rf"\b{palabra}\b"
color = "\033[41m"
#matchs = re.findall(regex, normal)
#print(matchs)
final = re.sub(regex, f"{color}{palabra}\033[0m", normal)
print(final)

def resaltar_palabra(texto, palabra, color_fondo="\033[43m"):  # Fondo amarillo por defecto
    # Expresión regular para encontrar la palabra exacta (evita reemplazar dentro de otras palabras)
    patron = rf'\b{re.escape(palabra)}\b'
    
    # Reemplazar la palabra por su versión coloreada
    texto_modificado = re.sub(patron, f"{color_fondo}{palabra}\033[0m", texto)

    return texto_modificado

# Ejemplo de uso
texto = " Python es un lenguaje genial. Me encanta Pythone!"
palabra_resaltar = "Python"

print(resaltar_palabra(texto, palabra_resaltar, "\033[41m"))  # Fondo rojo


######################################################################################################
def resaltar_coincidencias(texto, patrones_colores):
    """
    Resalta en el texto todas las coincidencias de varias expresiones regulares con distintos colores de fondo.
    
    :param texto: Cadena de texto a analizar.
    :param patrones_colores: Lista de tuplas (expresión regular, código ANSI de color).
    :return: Texto modificado con colores en las coincidencias.
    """
    texto_modificado = texto

    for patron, color_fondo in patrones_colores:
        texto_modificado = re.sub(
            patron, 
            lambda match: f"{color_fondo}{match.group(0)}\033[0m", 
            texto_modificado
        )

    return texto_modificado

# Ejemplo de uso
texto = "Python es increíble! Tengo 2 gatos y 1 perro. Mi correo es email@ejemplo.com."

# Lista de patrones y colores (fondo)
patrones_colores = [
    (r'\bPython\b', '\033[41m'),     # "Python" con fondo rojo
    (r'\d+', '\033[42m'),            # Números con fondo verde
    (r'\b\w+@\w+\.\w+\b', '\033[44m') # Correos electrónicos con fondo azul
]

print(resaltar_coincidencias(texto, patrones_colores))

