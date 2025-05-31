# code from claude :)
import random
import math
import os

def is_perfect_square(n):
    if n < 0:
        return False
    root = int(math.sqrt(n))
    return root * root == n

def generate_non_square(max_val):
    while True:
        val = random.randint(1, max_val)
        if not is_perfect_square(val):
            return val

def generate_testcase(subtask, case_num):
    MOD = 10**9 + 7
    
    if subtask == 1:
        # a=1, b=c=d=e=0, 1^n
        n = random.randint(1, 10**18)
        return f"{n} 1 0 0 0 0"
    
    elif subtask == 2:
        # n=0, (a+b√c+d√e)^0 = 1
        a = random.randint(0, 10**5)
        b = random.randint(0, 10**5)
        d = random.randint(0, 10**5)
        c = generate_non_square(10**5)
        e = generate_non_square(10**5)
        while c == e or c == 1:
            c = generate_non_square(10**5)
        return f"0 {a} {b} {c} {d} {e}"
    
    elif subtask == 3:
        # n=2, (a+b√c+d√e)^2
        n = 2
        a = random.randint(0, 10**5)
        b = random.randint(0, 10**5)
        d = random.randint(0, 10**5)
        c = generate_non_square(10**5)
        e = generate_non_square(10**5)
        while c == e or c == 1:
            c = generate_non_square(10**5)
        return f"{n} {a} {b} {c} {d} {e}"
    
    elif subtask == 4:
        # b=c=d=e=0且n≤10^6
        n = random.randint(1, 10**6)
        a = random.randint(1, 10**5)
        return f"{n} {a} 0 0 0 0"
    
    elif subtask == 5:
        # b=c=d=e=0, a^n
        n = random.randint(1, 10**18)
        a = random.randint(1, 10**5)
        return f"{n} {a} 0 0 0 0"
    
    elif subtask == 6:
        # c=2, a=d=e=0, (b√2)^n
        n = random.randint(1, 10**18)
        b = random.randint(1, 10**5)
        return f"{n} 0 {b} 2 0 0"
    
    elif subtask == 7:
        # c=2, d=e=0, (a+b√2)^n
        n = random.randint(1, 10**18)
        a = random.randint(0, 10**5)
        b = random.randint(0, 10**5)
        return f"{n} {a} {b} 2 0 0"
    
    elif subtask == 8:
        # a=0,n≤10^6, (b√c+d√e)^n
        n = random.randint(1, 10**6)
        b = random.randint(1, 10**5)
        d = random.randint(1, 10**5)
        c = generate_non_square(10**5)
        e = generate_non_square(10**5)
        while c == e or c == 1:
            c = generate_non_square(10**5)
        return f"{n} 0 {b} {c} {d} {e}"
    
    elif subtask == 9:
        # a=0, (b√c+d√e)^n
        n = random.randint(1, 10**18)
        b = random.randint(1, 10**5)
        d = random.randint(1, 10**5)
        c = generate_non_square(10**5)
        e = generate_non_square(10**5)
        while c == e or c == 1:
            c = generate_non_square(10**5)
        return f"{n} 0 {b} {c} {d} {e}"
    
    elif subtask == 10:
        # a,b,c,d,e≤10, n≤10
        n = random.randint(1, 10)
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        d = random.randint(0, 10)
        c = generate_non_square(10)
        e = generate_non_square(10)
        while c == e or c == 1:
            c = generate_non_square(10)
        return f"{n} {a} {b} {c} {d} {e}"
    
    elif subtask == 11:
        # n≤10^6
        n = random.randint(1, 10**6)
        a = random.randint(0, 10**5)
        b = random.randint(0, 10**5)
        d = random.randint(0, 10**5)
        c = generate_non_square(10**5)
        e = generate_non_square(10**5)
        while c == e or c == 1:
            c = generate_non_square(10**5)
        return f"{n} {a} {b} {c} {d} {e}"
    
    elif subtask == 12:
        # as statement
        n = random.randint(1, 10**18)
        a = random.randint(0, 10**5)
        b = random.randint(0, 10**5)
        d = random.randint(0, 10**5)
        c = generate_non_square(10**5)
        e = generate_non_square(10**5)
        while c == e or c == 1:
            c = generate_non_square(10**5)
        return f"{n} {a} {b} {c} {d} {e}"

def generate_all_testcases():
    """生成所有子任務的測試資料"""
    subtask_config = [
        (1, 3),   # 子任務1: 3個測試案例
        (2, 3),   # 子任務2: 3個測試案例
        (3, 5),   # 子任務3: 5個測試案例 
        (4, 3),   # 子任務4: 3個測試案例
        (5, 5),   # 子任務5: 5個測試案例 
        (6, 3),   # 子任務6: 3個測試案例
        (7, 5),   # 子任務7: 5個測試案例 
        (8, 3),   # 子任務8: 3個測試案例
        (9, 3),   # 子任務9: 3個測試案例
        (10, 2),  # 子任務10: 2個測試案例
        (11, 4),  # 子任務11: 4個測試案例
        (12, 6),  # 子任務12: 6個測試案例 
    ]
    
    if not os.path.exists('testdata'):
        os.makedirs('testdata')
    
    total_cases = 0
    
    for subtask, case_count in subtask_config:
        print(f"生成子任務 {subtask} 的測試資料...")
        
        for case in range(case_count):
            testcase = generate_testcase(subtask, case + 1)
            filename = f'testdata/subtask{subtask:02d}_case{case+1:02d}.in'
            
            with open(filename, 'w') as f:
                f.write(testcase + '\n')
            
            print(f"  生成: {filename}")
            print(f"    內容: {testcase}")
            total_cases += 1
    
    print(f"\n總共生成 {total_cases} 個測試案例")
    
    # 生成一些範例測試資料（與題目範例相同）
    examples = [
        "3 2 0 3 0 5",  # 範例1: (2+0√3+0√5)^3 = 8
        "2 3 1 2 0 7",  # 範例2: (3+1√2+0√7)^2 = 11 6 0 0
        "2 1 2 3 3 2",  # 範例3: (1+2√3+3√2)^2 = 31 4 6 12
    ]
    
    for i, example in enumerate(examples):
        filename = f'testdata/example{i+1}.in'
        with open(filename, 'w') as f:
            f.write(example + '\n')
        print(f"生成範例: {filename} - {example}")

if __name__ == "__main__":
    random.seed(42)  # 設定隨機種子以確保可重現性
    generate_all_testcases()
    print("\n測資生成完成！")
    print("所有測試檔案已保存在 'testdata' 目錄中")