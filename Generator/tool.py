import os
def conv(x):
    s = str(x)
    while len(s) < 3: s = '0' + s
    return s

def compile(x):
    os.system(f"g++ -std=c++17 -o sol {x}")

def duplicate(src):
    for i in range(100):
        j = conv(i)
        with open(f"{src}/{j}.in", "r") as cin, open(f"{i+1}.in", "w") as out:
            for line in cin:
                out.write(line)

        with open(f"{src}/{j}.out", "r") as cin, open(f"{i+1}.out", "w") as out:
            for line in cin:
                out.write(line)

def delete(src):
    os.system(f"rm {src}")