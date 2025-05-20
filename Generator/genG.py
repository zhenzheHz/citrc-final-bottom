import random
from tool import *

p14 = 10**10

def generate(id, N = -1, limit = 200000, M1 = False, LM = 2*p14):
    n = random.randint(2, limit)
    if N != -1: n = N
    p = [str(random.randint(1,10**4)) for _ in range(n)]
    line = " ".join(p)
    x = LM // n
    m = []
    if M1: m = ["1" for _ in range(n)]
    else: m = [str(random.randint(1,x)) for _ in range(n)]
    line2 = " ".join(m)
    with open(f"{conv(id)}.in","w") as file:
        file.write(f"{n}\n")
        file.write(f"{line}\n")
        file.write(f"{line2}")

# case 1 : sample case
# case 2 : n = 2
# case 3 : n = 3
# case 4 : n <= 100
# case 5 : Mi = 1
# case 6 : sum{Mi} <= 500000
# case 7 : as statement
# score : 3, 3, 2, 3, 3, 5, 5

for test in range(3,24):
    if test < 6: generate(test,N = 2)
    elif test < 8: generate(test,N = 3)
    elif test < 11: generate(test,limit = 100)
    elif test < 14: generate(test,M1 = True)
    elif test < 19: generate(test, LM = 500000)
    else : generate(test)