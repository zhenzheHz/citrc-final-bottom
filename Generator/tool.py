import os
import random
def conv(x):
    s = str(x)
    while len(s) < 3: s = '0' + s
    return s

def compile(x):
    os.system(f"g++ -std=c++17 -o sol {x}")

def duplicate(src, x = 0, y = 100):
    for i in range(x,y):
        j = conv(i)
        with open(f"{src}/{j}.in", "r") as cin, open(f"{i+1}.in", "w") as out:
            for line in cin:
                out.write(line)

        with open(f"{src}/{j}.out", "r") as cin, open(f"{i+1}.out", "w") as out:
            for line in cin:
                out.write(line)

def delete(src):
    os.system(f"rm {src}")


def Random(a,b):
    return random.randint(a,b)