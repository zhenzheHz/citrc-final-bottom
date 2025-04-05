from tool import *

path = "/Users/user/Desktop/CITRC-final/113-B/Testcases/B.DianSh1ng"

duplicate(path)

os.system("zip CJtestB.zip *.in *.out")

delete("*.in *.out")