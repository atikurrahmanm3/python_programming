import random

name = ['a', 'b', 'c', 'd', 'e', 'f', '@', '#', '$', '&', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '0', '1', '2', '3', '4', '5', '6', '7', '9']

choice = " "

for i in range(1, 9):
    choice += random.choice(name)
print(f" {choice} \n")
