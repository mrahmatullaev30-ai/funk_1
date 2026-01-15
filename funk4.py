import os
os.system('cls')
my_dict = {
    "t": 3,
    "p": 1,
    "y": 2,
    "o": 5,
    "h": 4,
    "n": 6,
}

sorted_keys = sorted(my_dict, key=my_dict.get)

for key in sorted_keys:
    print(key)