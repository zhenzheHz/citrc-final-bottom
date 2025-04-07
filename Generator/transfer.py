from tool import *

path = "/Users/user/Desktop/CITRC-final/113-B/Testcases/H.Goodbye"

duplicate(path)

os.system("zip CJtestH.zip *.in *.out")

delete("*.in *.out")