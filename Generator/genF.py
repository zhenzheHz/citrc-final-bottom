import random
import string
from tool import *

alpha = string.ascii_letters

def generate(id, space = True, X = -1):
    # n = random.randint(1,1000)
    # if limit_n: n = assign_n
    x = random.randint(0,25)
    if X != -1: x = X
    with open(f"{conv(id)}.in","w") as file:
        file.write(f"{x}\n")
        # for i in range(n):
        line = ""
        for _ in range(18):
            ch = random.choices(alpha, k = random.randint(1,10))
            word = "".join(ch)
            line += word
            if space and _!=8: line += " "
        file.write(line + '\n')


# case 1 : length(S) = 1
# case 2 : x = 0 , no space 
# case 3 : x = 2 , no space 
# case 4 : x = 0
# case 5 : x = 2
# case 6 : as statement
# score : 2, 2, 5, 2, 5, 5

for test in range(21):
    if test < 2: 
            with open(f"{conv(test)}.in","w") as file:
                 file.write(f"{random.randint(0,25)}\n{random.choice(alpha)}")
    elif test < 4:
         generate(test, space = False, X = 0)
    elif test < 9:
         generate(test, space = False, X = 2)
    elif test < 11:
         generate(test, X = 0)
    elif test < 16:
         generate(test, X = 2)
    else:
         generate(test)