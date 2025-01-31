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