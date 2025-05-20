import random
import string
from tool import *

alpha = string.ascii_letters
sign = ".,"

def generate_subtask2(id):
    n = random.randint(500,1000)
    lst = [random.choice(alpha) for _ in range(n)]
    with open(f"{conv(id)}.in","w") as file:
        file.write(f"{n}\n")
        for sen in lst:
            file.write(f"{sen}\n")

def generate(id,space = True, limit_n = False, assign_n = 1):
    n = random.randint(1,1000)
    if limit_n: n = assign_n
    with open(f"{conv(id)}.in","w") as file:
        file.write(f"{n}\n")
        for i in range(n):
            line = ""
            for _ in range(9):
                ch = random.choices(alpha + sign, k = random.randint(1,10))
                word = "".join(ch)
                line += word
                if space and _!=8: line += " "
            file.write(line + '\n')

# case 1 : sample case
# case 2 : length(S) = 1
# case 3 : n = 1 not space
# case 4 : n = 1 but space
# case 5 : n = 2 not space
# case 6 : not space
# case 7 : as statement
# score : 2, 2, 5, 5, 3, 5, 5

for test in range(2,27):
    if test < 4: generate_subtask2(test)
    elif test < 9: generate(test,space = False, limit_n = True, assign_n = 1)
    elif test < 14: generate(test,limit_n = True, assign_n = 1)
    elif test < 17: generate(test,space = False, limit_n = True, assign_n = 2)
    elif test < 22: generate(test,space = False)
    else: generate(test)