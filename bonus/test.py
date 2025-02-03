import re
import sys
import math

print("test")
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

def get_monomial_bonus(string:str):
    monomials:list
    regexs = [r"([+-])",                                #sign
            r"\s*\d+(\.\d+)? \* X(?:\^\d+\s*$|\s*$)",   #complete monomial
            r"\s*\d+\s*$",                              #only coefficient
            r"\s*\d+(\.\d+)? \* X \d+\s*$",             #no exponent
            r"\s*X\^\d+\s*$"]                           #no coefficient

    split_string = [string for string in re.split(regexs[0], string) if string]
    if split_string[0] not in ["-", "+"]:
        split_string.insert(0, "+")
    print("split:", split_string)
    sign = ""
    for piece in split_string:
        for regex in regexs:
            #print(f"{piece} try [{regex}]")
            span = re.match(regex, piece)
            if span != None:
                print(f"{piece} mach[{regex}]")
                break

    #return monomials


print("--- get monomials ---")
get_monomial_bonus(sys.argv[1])

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
