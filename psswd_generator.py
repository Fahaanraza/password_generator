import random
from typing import List
pas = int(input("enter the length of password: "))
digit = int(input("enter the number of digits: "))
sym = int(input("enter the number of symbols: "))
alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
num = list("1234567890")
symb = ["!", "#", "@", "$", "%", "^", "&", "*", "?"]
wow = []
for i in range(0, pas-digit-sym+1):
    wow.append(random.choice(alpha))
for i in range(0, digit+1):
    wow.append(random.choice(num))
for i in range(0, sym+1):
    wow.append(random.choice(symb))
random.shuffle(wow)
password = ""
for char in wow:
    password += char
print(f"your pass is: {password}")
