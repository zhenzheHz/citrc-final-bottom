import random
from tool import *

digit = "023456789"

def generate(id, haveOne = True, limit = 10**6):
    x = random.randint(2,limit)
    ch = digit
    if haveOne : ch += "1111111"
    # random.shuffle(ch)
    num = random.choices(ch, k = x)
    while num[0] == "0": num[0] = str(random.randint(2,9))
    line = "".join(num)
    with open(f"{conv(id)}.in","w") as file: file.write(line)

def generate_subtask4(id):
    x = random.randint(1,10**6)
    num = random.choices(digit, k = x)
    while num[0] == "0": num[0] = str(random.randint(2,9))
    change = random.randint(0,x-1)
    num[change] = "1"
    line = "".join(num)
    with open(f"{conv(id)}.in","w") as file: file.write(line)

# case 1 : sample test
# case 2 : 1 <= S <= 10
# case 3 : no one
# case 4 : 1 appears only once or never
# case 5 : 1 <= S <= 10^5
# case 6 : as statement
# score : 5, 3, 2, 3, 5, 5

for test in range(5,23):
    if test < 8: 
        with open(f"{conv(test)}.in","w") as f: f.write(f"{test-4}")
    elif test < 10: generate(test, haveOne=False)
    elif test < 13: generate_subtask4(test)
    elif test < 18: generate(test,limit = 5)
    else: generate(test)