import tool

# case 1 : (10) x = 0
# case 2 : (10) y = 10
# case 3 : (30) y = 2
# case 4 : (10) y = x^k(k is N)
# case 5 : (40) as statement
# 1, 4, 10, 5, 20

def generate(id, X = -1, Y = -1):
    x,y = tool.Random(0,10**18), tool.Random(2,36)
    if X != -1: x = X
    if Y != -1: y = Y
    with open(f"{tool.conv(id)}.in", "w") as file:
        file.write(f"{x} {y}")

for test in range(40):
    if test < 1: generate(test, X = 0)
    elif test < 5: generate(test, Y = 10)
    elif test < 15: generate(test, Y = 2)
    elif test < 20: 
        a = tool.Random(11,30)
        b = tool.Random(1,10)
        generate(test, X = a**b, Y = a)
    else: generate(test)