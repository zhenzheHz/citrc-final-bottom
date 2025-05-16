import tool

threshold = 10**5

def generate(id, limit = [-1,-1,-1,-1], upN = -1):
    n = str(tool.Random(10**16, 10**18))
    for i in range(len(limit)):
        if limit[i] == -1: limit[i] = tool.Random(-threshold, threshold)
    limit[2] = abs(limit[2])
    limit = [str(i) for i in limit]
    if upN == 2: n = 2
    elif upN != -1: n = tool.Random(1000, threshold)
    line = " ".join(limit)
    with open(f"{tool.conv(id)}.in","w") as file:
        file.write(f"{n} " + line)

# case 1 : (5) a = 1, b = d = 0
# case 2 : (10) b = d = 0
# case 3 : (15) a = d = 0, c = 2
# case 4 : (20) b = 0
# case 5 : (20) b = 1, d = 0
# case 6 : (20) d = 0
# case 7 : (15) n = 2
# case 8 : (15) n <= 10^5
# case 9 : (180) as statement
# 5, 5, 5, 5, 5, 5, 5, 5, 10

for test in range(50):
    if test < 5: generate(test, [1,0,-1,0])
    elif test < 10: generate(test, [-1,0,-1,0])
    elif test < 15: generate(test, [1,-1,2,0])
    elif test < 20: generate(test, [-1,0,-1,-1])
    elif test < 25: generate(test, [-1,1,-1,0])
    elif test < 30: generate(test, [-1,-1,-1,0])
    elif test < 35: generate(test, upN = 2)
    elif test < 40: generate(test, upN = threshold)
    else: generate(test)