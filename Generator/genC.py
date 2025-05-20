import random
from tool import *

max_p = 10**12

def generate_subtask4(id):
    with open(f"{conv(id)}.in","w") as file:
        file.write(f"{2}\n")
        if id % 2 == 0 : file.write(f"{random.randint(1,max_p)} 0 0")
        else : file.write(f"{random.randint(-max_p,-1)} 0 0")

def generate(id, assign = -1):
    n = random.randint(0,200000)
    if assign != -1: n = assign
    p = [str(random.randint(-max_p,max_p))]
    while p[0] == "0": p[0] = str(random.randint(-max_p,max_p))
    for i in range(n):
        if random.randint(1,5) == 1:
            p.append("0")
        else:
            p.append(str(random.randint(-max_p,max_p)))
    line = " ".join(p)
    with open(f"{conv(id)}.in","w") as file:
        file.write(f"{n}\n")
        file.write(line)

# case 1 : sample case
# case 2 : n = 0
# case 3 : n = 1
# case 4 : n = 2, p1 = p0 = 0
# case 5 : n = 2
# case 6 : -100 <= pi <= 100
# case 7 : as statement
# score : 4, 3, 3, 3, 3, 5, 7

for test in range(4,28):
    if test < 7: generate(test,0)
    elif test < 10: generate(test,1)
    elif test < 13: generate_subtask4(test)
    elif test < 16: generate(test,2)
    elif test < 21: 
        max_p = 100
        generate(test)
    else :
        max_p = 10**12
        generate(test)