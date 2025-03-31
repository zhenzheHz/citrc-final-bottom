import random
from tool import get_id

def generate_caseA(i):
    n = random.randint(50,200000)
    x = random.randint(3, n-2)
    t = [random.randint(1,10**15) for _ in range(n)]
    if i < 20: t = sorted(t)
    t = [str(i) for i in t]
    line = " ".join(t)
    with open(f"{get_id(i)}.in", "w") as file:
        file.write(f"A {x}\n")
        file.write(f"{n}\n")
        file.write(line)

def generate_caseB(i):
    x = random.randint(50, 10**12)
    with open(f"{get_id(i)}.in", "w") as file:
        file.write(f"B {x}")

for i in range(2,10):
    j = i+1
    x = j ** 3 + j + random.randint(-2,2)
    with open(f"{get_id(i)}.in", "w") as file:
        file.write(f"B {x}")

for i in range(10, 30):
    generate_caseA(i)

for i in range(30, 50):
    generate_caseB(i)

for i in range(50,100):
    if i%2 == 1:
        generate_caseA(i)
    else:
        generate_caseB(i)