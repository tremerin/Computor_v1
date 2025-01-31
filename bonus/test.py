import re
import sys

print("test")
regex = r"([+-])" 
if len(sys.argv) == 2:
    #list comprehension
    split_string = [string for string in re.split(regex, sys.argv[1]) if string]
    if split_string[0] not in ["-", "+"]: 
        split_string.insert(0, "+")
    print(split_string)


valid = r"\s*\d+(\.\d+)? \* X(?:\^\d+\s*$|\s*$)"
for string in split_string:
    span = re.match(valid, string)
    if span == None:
        print(f"{string}: false")
    else:
        print(f"{string}: true")


#minimo comun multiplo
def mcm(nums:list):
    max_multiplo = nums[0]
    mach:bool = False
    if len(nums) == 1:
        return max_multiplo
    for i in range(len(nums) - 1):
        print(i)
        while mach == False:
            multiplo = max(max_multiplo, nums[i + 1])
            if multiplo % nums[i] == 0 and multiplo % nums[i + 1] == 0:
                max_multiplo = multiplo
                mach = True
            else:
                max_multiplo += 1
        
    return max_multiplo


#maximo comun divisor
def mcd(nums:list):
    pass

nums = [2, 6, 5]
print(f"mcm de: {nums}")
print(mcm(nums))
