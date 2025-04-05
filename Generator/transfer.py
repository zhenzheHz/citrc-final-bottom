from tool import *

path = "/Users/user/Desktop/CITRC-final/113-B/Testcases/C.PseudoDifferentiable"

duplicate(path)

os.system("zip CJtestC.zip *.in *.out")

delete("*.in *.out")