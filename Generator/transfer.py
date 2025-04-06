from tool import *

path = "/Users/user/Desktop/CITRC-final/113-B/Testcases/D.No 1 can solve this problem"

duplicate(path)

os.system("zip CJtestD.zip *.in *.out")

delete("*.in *.out")