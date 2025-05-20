import tool
import math

def create(test_id,A,B,C):
    with open(f"{tool.conv(test_id)}.in","w") as file:
        file.write(f"{A} {B} {C}")

def generate_subtask1(id):
    a = tool.Random(1,500)
    c = tool.Random(100,1000)
    up = int(math.sqrt(4*a*c)+1)
    b = tool.Random(0, up)
    if tool.Random(0,1) == 1: b *= -1
    create(id, a, b, c)

def generate_subtask2(id):
    a = tool.Random(1,10)
    alpha,beta = tool.Random(-100,100), tool.Random(-500,100)
    b = -1 * (alpha + beta) * a
    c = alpha * beta * a
    create(id, a, b, c)

def generate_subtask3(id):
    a = tool.Random(1,500)
    c = tool.Random(100,1000)
    low = int(math.sqrt(4*a*c)+1)
    b = tool.Random(low, 5000)
    create(id, a, b, c)

# case 1 : b*b-4ac<0
# case 2 : two roots are integar
# case 3 : as statement
# 5 / 5 / 10

for test in range(20):
    if test < 5 : generate_subtask1(test)
    elif test < 10 : generate_subtask2(test)
    else : generate_subtask3(test)