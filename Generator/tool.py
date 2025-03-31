import os
def get_id(x):
    s = str(x)
    while len(s) < 3: s = '0' + s
    return s

def compile(x):
    os.system(f"g++ -std=c++17 -o sol {x}")

def copy_testcases(src):
    for i in range(100):
        j = get_id(i)
        with open(f"{src}/{j}.in", "r") as cin, open(f"{i+1}.in", "w") as out:
            for line in cin:
                out.write(line)

        with open(f"{src}/{j}.out", "r") as cin, open(f"{i+1}.out", "w") as out:
            for line in cin:
                out.write(line)
