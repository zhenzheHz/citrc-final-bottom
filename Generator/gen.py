import os
from tool import *
start,end = 2,100

# solution = "/Users/user/Desktop/CITRC-final/113-B/Solutions/A.Unattainable/AC.cpp"
# compile(solution)

for i in range(start,end):
    x = conv(i)
    os.system(f"./sol < {x}.in > {x}.out")

# delete("sol")