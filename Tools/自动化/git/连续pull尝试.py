import os
import time
import subprocess
import tkinter as tk
from tkinter import filedialog
from colorama import init, Fore

# --- init ---
init(autoreset=True)
root = tk.Tk()
root.withdraw()
# ------------

'''
1. 获取工作目录
2. 检测是否与远程仓库有差异
3. 如果是，执行3.1.1；否则执行3.2.1
3.1.1 尝试pull到本地仓库
3.1.2 如果成功，显示提醒；如果失败，检测是否为网络错误，如果是则执行3.1.3
3.1.3 计数+1，等待10秒后重新执行3.1.1
3.2.1 (已是最新)给与提示
'''

def has_unpulled_commits(working_dir):  
    result = subprocess.run('git cherry -v', shell=True, capture_output=True, text=True, cwd=working_dir)
    
    while True:
        if result.returncode == 0 and result.stdout is not None: # 检查命令是否成功执行并且有输出
            output = result.stdout.strip()
            print("[info]检测到差异：", output)
            return True
        else:
            print("[ERROR] 获取差异时出错")


def pull_commits(working_dir): # pull提交
    result = subprocess.run('git pull', shell=True, capture_output=True, text=True, cwd=working_dir)
    if result.returncode == 0:
        return "pull successful"
    else:
        return result.stderr
    
def is_network_error(stderr):# 判断错误类型
    network_error_keywords = [
        "unable to access",
        "Could not resolve host",
        "Failed to connect",
        "Operation timed out",
        "early EOF",
        "RPC failed"
    ]
    for keyword in network_error_keywords:
        if keyword in stderr:
            return True
    return False

def main():
    working_dir = filedialog.askdirectory("请选择仓库目录")
    print(f"{Fore.BLUE}✓{Fore.RESET} 选择的仓库目录: {working_dir}")
    
    while True:
        time_counter = int(input("请输入每次尝试的间隔(秒)：", end=""))
        # 检测适用性
        if time_counter <= 1:
            print(f"{Fore.RED}✕{Fore.RESET} 间隔过短！请指定一个大于1的值！")
        else:
            print(f"{Fore.BLUE}✓{Fore.RESET} 已设置间隔时间: {time_counter}")
            break
    
    counter = 0

    while True:
        if has_unpulled_commits(working_dir):
            counter += 1
            pull_output = pull_commits(working_dir)
            if "pull successful" in pull_output:
                print(f"{Fore.GREEN}✓{Fore.RESET} 拉取成功！！")
                break
            elif is_network_error(pull_output):
                print(f"{Fore.YELLOW}⚠{Fore.RESET} 第 {Fore.BLUE}{counter}{Fore.RESET} 次拉取尝试失败")
                print(f"原因: {Fore.RED}{pull_output}{Fore.RESET}")
                temp = time_counter
                for i in range(time_counter, 0, -1):
                    print(f"\r{i}秒后重试...", end="")
                    time.sleep(1)
                print("\r")
                time_counter = temp # 还原秒数设置
            else:
                print(f"{Fore.RED}✕{Fore.RESET} 第 {Fore.BLUE}{counter}{Fore.RESET} 次拉取尝试失败，出现了非已知网路问题\n{Fore.BLUE}[提示]{Fore.RESET} 如果你确定这是网络问题，请提交issue或者PR，感谢！")
                print(f"原因: {Fore.RED}{pull_output}{Fore.RESET}")
                t = input("请确认是否继续尝试: ")
                if t.lower() not in ["y", "yes", "是", "继续", "确认"]:
                    print(f"{Fore.RED}✕{Fore.RESET} 由于检测到非网络错误，已终止程序")
                    break
        else:
            print(f"{Fore.GREEN}✓{Fore.RESET} 本地仓库已是最新，无需拉取")
    print(f"{Fore.BLUE}[info]{Fore.RESET} 一共执行了 {Fore.BLUE}{counter}{Fore.RESET} 次pull")

if __name__ == "__main__":
    main()
    input ("按Enter键退出...")
