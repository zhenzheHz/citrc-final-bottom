from tool import *

path = "/Users/user/Desktop/CITRC-final/113-B/Testcases/E.Today's Kahoot"

duplicate(path)

os.system("zip CJtestE.zip *.in *.out")

delete("*.in *.out")