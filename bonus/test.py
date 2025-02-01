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
for string in split_string:
    span = re.match(valid, string)
    if span == None:
        print(f"{string}: false")
    else:
        print(f"{string}: true")


#minimo comun multiplo
def mcm(nums:list):
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


#maximo comun divisor
def mcd(nums:list):
    pass

nums = [2, 6, 4, 5, 2]
print(f"mcm de: {nums}")
print(mcm(nums))
