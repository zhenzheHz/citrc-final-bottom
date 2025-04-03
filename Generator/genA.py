import random
from tool import *

def generate_caseA(id, sub2 = False, limit = False):
    lower_n = 100000
    if limit: lower_n = 200000
    n = random.randint(lower_n,200000)
    x = random.randint(50,n-3)
    t = [random.randint(1,10**15) for _ in range(n)]
    if sub2: t = sorted(t)
    t = [str(i) for i in t]
    line = " ".join(t)
    with open(f"{conv(id)}.in","w") as file:
        file.write("A\n")
        file.write(f"{n} {x}\n")
        file.write(line)
    
def generate_caseB(id,sub3 = False,sub4 = False):
    a,b = random.randint(0,100),random.randint(0,10**9)
    x = random.randint(10**10,10**18)
    if sub3: a,b = 0,0
    if sub4: 
        a = random.randint(0,100)
        b = random.randint(0,100)
        x = random.randint(202,10**8)
    with open(f"{conv(id)}.in","w") as file:
        file.write(f"B\n{x} {a} {b}")

# case 1 : sample test
# case 2 : A & <t> is sorted
# case 3 : B & a = b = 0
# case 4 : B & x <= 10^8
# case 5 : A
# case 6 : B
# case 7 : as statement
# score : 2 / 8 / 10 / 10 / 20 / 20 / 30

for test in range(2,10):
    full = test > 7
    generate_caseA(test,sub2 = True,limit = full)
for test in range(10,20):
    generate_caseB(test,sub3 = True)
for test in range(20,30):
    generate_caseB(test,sub4 = True)
for test in range(30,50):
    generate_caseA(test,limit = test>40)
for test in range(50,70):
    generate_caseB(test)
for test in range(70,100):
    if random.randint(1,2) == 1:
        generate_caseA(test,limit = True)
    else:
        generate_caseB(test)