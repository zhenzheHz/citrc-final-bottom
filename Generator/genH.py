import tool

for test in range(16):
    with open(f"{tool.conv(test)}.in","w") as file:
        file.write(f"{test}")
    with open(f"{tool.conv(test)}.out","w") as file:
        pass