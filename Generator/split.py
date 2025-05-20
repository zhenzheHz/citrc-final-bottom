from Generator.tool import *
import os
path = "/Users/user/Desktop/CITRC-final/113-B/Testcases/A.Unattainable"

# score : 2 / 8 / 10 / 10 / 20 / 20 / 30

task = [2,8,10,10,20,20,30]

current = 0
task_count = 1

for tk in task:
    duplicate(path, current, current+tk)
    current += tk;
    os.system(f"zip subtask{task_count}.zip *.in *.out")
    delete("*.in *.out")
    task_count += 1