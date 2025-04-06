import random
from tool import *

def generate_task1(id, lim_a = -1, lim_b = -1, lim_p = -1):
    a = random.randint(1,10**9)
    b = random.randint(1,10**18)
    p = random.randint(3,10**9)
    if lim_a != -1: a = lim_a
    if lim_b != -1: b = random.randint(1,lim_b)
    if lim_p != -1: p = lim_p
    with open(f"{conv(id)}.in","w") as file:
        file.write(f"1 {a} {b} {p}")
    
def generate_task2(id, lim_n = 10**18):
    n = random.randint(1,lim_n)
    with open(f"{conv(id)}.in","w") as file:
        file.write(f"2 {n}")

def generate_task3(id, lim_S = -1):
    S = random.randint(0, 2**61)
    if lim_S != -1: S = lim_S
    with open(f"{conv(id)}.in","w") as file:
        file.write(f"3 {S}")

# case 1 : Q = 1, a = 2, p = 10
# case 2 : Q = 1, b <= 10^5
# case 3 : Q = 2, n <= 15
# case 4 : Q = 2, n <= 2x10^5
# case 5 : Q = 3, S = 2^k (0<=k<=31)
# case 6 : Q = 1
# case 7 : Q = 2
# case 8 : Q = 3
# case 9 : as statement
# score : 8 / 8 / 8 / 8 / 8 / 20 / 20 / 20 / 100

for test in range(100):
    if test < 4: generate_task1(test, lim_a = 2, lim_p = 10)
    elif test < 8: generate_task1(test, lim_b = 100000)
    elif test < 12: generate_task2(test, lim_n = 15)
    elif test < 16: generate_task2(test, lim_n = 200000)
    elif test == 16: generate_task3(test, lim_S = 0)
    elif test < 20: generate_task3(test, lim_S = 2**(random.randint(1,30)))
    elif test < 30: generate_task1(test)
    elif test < 40: generate_task2(test)
    elif test < 50: generate_task3(test)
    elif test == 50: generate_task3(test, lim_S = 0)
    else:
        if test % 3 == 0: generate_task1(test)
        elif test % 3 == 1: generate_task2(test)
        else: generate_task3(test)