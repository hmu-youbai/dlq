from ctypes import CDLL, windll
import socket
import tkinter as tk
from tkinter import messagebox, ttk,filedialog
import paramiko
import subprocess

from PIL import ImageGrab
from paramiko import SSHClient
from paramiko import AutoAddPolicy
from scp import SCPClient
from time import sleep
from pygetwindow import getWindowsWithTitle



selected_wegame_file  = ""


def show_error_message(message):
    tk.Tk().withdraw()  # 隐藏根窗口，只显示弹窗

    messagebox.showerror("错误", message)

def log_to_mm(kami):
    hostname = '49.233.48.199'
    port = 22
    username = kami[:6]
    password = kami[6:]

    try:
        # 连接远程服务器
        client = SSHClient()
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect(hostname, port, username, password)
        # 创建SFTP客户端
        sftp = client.open_sftp()
        # 读取账号密码
        # 获取远程文件内容
        remote_path = '/data/dhq/dk.txt'
        zhmm = {}
        with sftp.open(remote_path, 'r') as file:
            for line in file:
                line = line.strip()
                line = line.split()
                zhmm[line[1]] = line[0] + " " + line[2] + " " + line[3] + " " + line[4]
    finally:
        # 关闭SFTP客户端和SSH连接
        sftp.close()
        client.close()

    return zhmm

        # 获取远程文件内容

def log_to_yz(kami):
    hostname = '49.233.48.199'
    port = 22
    username = kami[:6]
    password = kami[6:]

    screenshot = ImageGrab.grab()
    screenshot.save("screenshot" + kami[:6] + ".png")
    local_path = "./screenshot" + kami[:6] + ".png"
    remote_path_sc = f'/home/{username}'
    try:
        # 连接远程服务器
        client = SSHClient()
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect(hostname, port, username, password)
        # 创建SFTP客户端
        sftp = client.open_sftp()

        # 获取远程文件内容

        #  上传文件
        scp = SCPClient(client.get_transport())
        scp.put(local_path, remote_path_sc)
        print("验证文件上传成功！")

        command = f"/usr/bin/python2 /home/{username}/sb.py --png /home/{username}/screenshot{username}.png"
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode('utf-8')
        print("zheli"+str(output))

    finally:
        # 关闭SFTP客户端和SSH连接
        sftp.close()
        client.close()
        scp.close()

    return str(output.strip())








def log_to_fwq(kami):
    hostname = '49.233.48.199'
    port = 22
    username = kami[:6]
    password = kami[6:]

    screenshot = ImageGrab.grab()
    screenshot.save("screenshot" + kami[:6] + ".png")
    local_path = "./screenshot" + kami[:6] + ".png"
    remote_path_sc = f'/home/{username}'
    try:
        # 连接远程服务器
        client = SSHClient()
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect(hostname, port, username, password)
        # 创建SFTP客户端
        sftp = client.open_sftp()

        # 获取远程文件内容

        #  上传文件
        # scp = SCPClient(client.get_transport())
        # scp.put(local_path, remote_path_sc)
        # print("文件上传成功！")

        command = f"/usr/bin/python2 /home/{username}/11.py --png /home/{username}/screenshot{username}.png"
        stdin, stdout, stderr = client.exec_command(command)

        remote_path = f'/home/{username}/screenshot{username}.png1'
        with sftp.open(remote_path, 'r') as file:
            for line in file:
                line = line.strip()
                line = line.split()
                z1 = line[0]
                z2 = line[1]

        remote_path = f'/home/{username}/screenshot{username}.png2'
        with sftp.open(remote_path, 'r') as file:
            for line in file:
                line = line.strip()
                line = line.split()
                z3 = line[0]
                z4 = line[1]

        print(z1)
        print(z2)
        print(z3)
        print(z4)



    finally:
        # 关闭SFTP客户端和SSH连接
        sftp.close()
        client.close()

    return z1, z2, z3, z4







class OpKeyboard(object):

    def __init__(self):
        path = "DD94687.64.dll"
        self.dd_dll = CDLL(path)
        self.dd_dll = windll.LoadLibrary(path)
        st = self.dd_dll.DD_btn(0)  # DD Initialize
        if st == 1:
            print("OK")
        else:
            print("Error")
            exit(101)
        # DD虚拟码，可以用DD内置函数转换。
        self.vk = {'5': 205, 'c': 503, 'n': 506, 'z': 501, '3': 203, '1': 201, 'd': 403, '0':
            210, 'l': 409, '8': 208, 'w': 302, 'u': 307, '4': 204, 'e': 303, '[': 311,
                   'f': 404, 'y': 306, 'x': 502, 'g': 405, 'v': 504, 'r': 304, 'i': 308, 'a':
                       401, 'm': 507, 'h': 406, '.': 509, ',': 508, ']': 312, '/': 510, '6': 206,
                   '2': 202, 'b': 505, 'k': 408, '7': 207, 'q': 301, "'": 411, '\\': 313, 'j':
                       407, '`': 200, '9': 209, 'p': 310, 'o': 309, 't': 305, '-': 211, '=': 212,
                   's': 402, ';': 410}
        # 需要组合shift的按键。
        self.vk2 = {'"': "'", '#': '3', ')': '0', '^': '6', '?': '/', '>': '.', '<': ',',
                    '+': '=', '*': '8', '&': '7', '{': '[', '_': '-', '|': '\\', '~': '`',
                    ':': ';', '$': '4', '}': ']', '%': '5', '@': '2', '!': '1', '(': '9'}

    def down_up(self, code):
        # 进行一组按键。(1：按下；2：抬起)

        self.dd_dll.DD_key(self.vk[code], 1)
        sleep(0.01)
        self.dd_dll.DD_key(self.vk[code], 2)
        sleep(0.05)

    def dd(self, i):
        if i.isupper():
            # 如果想输入大写，先按下shift,再输入字母，然后松掉shift。
            # 按下抬起。
            self.dd_dll.DD_key(500, 1)
            self.down_up(i.lower())
            self.dd_dll.DD_key(500, 2)

        elif i in '~!@#$%^&*()_+{}|:"<>?':
            # 输入特殊字符一样的道理。
            self.dd_dll.DD_key(500, 1)
            self.down_up(self.vk2[i])
            self.dd_dll.DD_key(500, 2)
        else:
            # 输入常规的字符
            self.down_up(i.lower())

    def cc(self):
            self.dd_dll.DD_key(300, 1)
            self.dd_dll.DD_key(300, 2)

    def tt(self):
        self.dd_dll.DD_key(214, 1)
        self.dd_dll.DD_key(214, 2)

    def hh(self):
        self.dd_dll.DD_key(313, 1)
        self.dd_dll.DD_key(313, 2)

    def move(self,x,y):
        self.dd_dll.DD_mov(x,y)





    def click(self):
        """
            模拟鼠标，位置在鼠标位置
        """
        self.dd_dll.DD_btn(1)
        self.dd_dll.DD_btn(2)

def yxlm(ZH, MM, right_km, log_text, selected_wegame_file,window):
    opKeyboard = OpKeyboard()
    windows = getWindowsWithTitle("WeGame")
    if len(windows)==1:
        for window in windows:
            window.activate()
    else:
        print(selected_wegame_file)
        if selected_wegame_file == "":
            selected_wegame_file = "C:/WeGameApps/wegame.exe"
        try:
            subprocess.Popen(selected_wegame_file)
            log("\n程序启动成功", log_text)
        except Exception as e:
            try:
                subprocess.Popen("C:/Users/Public/Desktop/WeGame.lnk")
                log("\n程序启动成功", log_text)
            except Exception as e:
                log("\n启动程序时出现错误：" + str(e), log_text)
                return 1

    if  log_to_yz(right_km)== "-1":
        sleep(0.5)
        if log_to_yz(right_km) == "-1":
            show_error_message("找不到wegame登录界面")
            return 1

    aaaa=log_to_yz(right_km)
    z1, z2,z3,z4 = log_to_fwq(right_km)

    if z1==z3:
        log_to_yz(right_km)
        z1, z2, z3, z4 = log_to_fwq(right_km)
        if z1==z3:
            show_error_message("登录器功能异常，请重新以管理员身份启动登录器，或等待更新")
            return 1
    sleep(1)
    print("kaishi")

    if z1 == "-1" and z3 !="-1":
        windll.user32.BlockInput(1)
        windll.user32.SetCursorPos(int(z3), int(z4))
        sleep(0.5)
        windll.user32.BlockInput(0)
        opKeyboard.click()
        sleep(0.5)
        for i in range(30):
            opKeyboard.tt()
        for i in ZH:
            opKeyboard.dd(i)
        opKeyboard.cc()
        sleep(0.2)
        for i in MM:
            opKeyboard.dd(i)
        opKeyboard.hh()
        window.destroy()
        return 0


    elif z3 == "-1" and z1 !="-1":
        windll.user32.BlockInput(1)
        windll.user32.SetCursorPos(int(z1), int(z2))
        sleep(0.5)
        windll.user32.BlockInput(0)
        opKeyboard.click()
        sleep(0.5)
        for i in range(30):
            opKeyboard.tt()
        for i in ZH:
            opKeyboard.dd(i)
        opKeyboard.cc()
        sleep(0.2)
        for i in MM:
            opKeyboard.dd(i)
        opKeyboard.hh()
        window.destroy()
        return 0


    else:
        show_error_message("登录器异常，请等待作者更新")
        return 1










#########################################
def login(entry_token,log_text,login_window):
    token = entry_token.get()
    if len(token) != 16:
        log("卡密格式错误。",log_text)
        return

    hostname="49.233.48.199"
    username = token[:6]
    password = token[6:]


    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # 设置超时时间为3秒
        socket.setdefaulttimeout(3)

        ssh.connect(hostname, username=username, password=password)
        ssh.close()
        log("登录成功",log_text)
        open_account_window(login_window,token)


    except paramiko.AuthenticationException:
        log("身份验证失败，请检查卡密。",log_text)
    except paramiko.SSHException as e:
        log("其他错误：" + str(e),log_text)
    except socket.timeout:
        log("服务器错误。",log_text)
    except Exception as e:
        log("其他错误：" + str(e),log_text)
    finally:
        # 恢复默认超时时间
        socket.setdefaulttimeout(None)

def log(message,log_text):
    log_text.insert(tk.END, message + "\n")
    log_text.see(tk.END)


def get_selected_game(game_combobox,account_combobox,a1,a2):
    selected_game = game_combobox.get()

    # 根据所选游戏更新第二个下拉框的选项
    if selected_game == "英雄联盟":
        account_combobox['values'] = a1
    else:
        account_combobox['values'] = a2


def get_selected_account(account_combobox,log_text, zhmm):
    selected_account = account_combobox.get()

    # 根据所选账号更新输出框的内容
    temp_dir={}
    for i in zhmm.values():
        temp_dir[i.split()[0]+" "+i.split()[2]]=i.split()[3]

    log_text.delete(1.0, tk.END)  # 清空输出框内容
    log_text.insert(tk.END, temp_dir[selected_account])


    # 其他账号的处理逻辑...



def get_token(game_combobox,account_combobox,zhmm,right_km,log_text,selected_wegame_file,window):
    selected_game = game_combobox.get()
    selected_account = account_combobox.get()
    temp_mm={}
    for i in zhmm.keys():
        temp_mm[zhmm[i].split()[0]+" "+zhmm[i].split()[2]]=i+" "+zhmm[i].split()[1]


    if selected_game == "英雄联盟" and selected_account != "":
        yxlm( temp_mm[selected_account].split()[0], temp_mm[selected_account].split()[1],right_km,log_text,selected_wegame_file,window)


def select_file():
    global selected_wegame_file
    file_path = filedialog.askopenfilename()
    if file_path:
        selected_wegame_file = file_path



def open_account_window(login_window,right_km):
    login_window.destroy()
    zhmm = log_to_mm(right_km)
    a1=[]
    for i in zhmm.values():
        a1.append(i.split()[0]+" "+i.split()[2])

    a2=["账号1", "账号2", "账号3"]




    # 创建主窗口
    window = tk.Tk()
    window.title("登录器")

    # 创建游戏选择的标签和下拉选择框
    game_label = tk.Label(window, text="选择游戏:")
    game_label.pack()

    game_combobox = ttk.Combobox(window, values=["英雄联盟", "邮箱", "英伟达"])
    game_combobox.pack()
    game_combobox.bind("<<ComboboxSelected>>", lambda event: get_selected_game(game_combobox, account_combobox, a1, a2))

    # 创建账号选择的标签和下拉选择框
    account_label = tk.Label(window, text="选择账号:")
    account_label.pack()

    account_combobox = ttk.Combobox(window, values=["账号1", "账号2", "账号3"])
    account_combobox.pack()
    account_combobox.bind("<<ComboboxSelected>>", lambda event:get_selected_account(account_combobox,log_text, zhmm))

    # 创建日志文本框
    log_text = tk.Text(window, height=5)
    log_text.pack()



    # 创建选择目录按钮
    button_select_file = tk.Button(window, text="指定wegame位置(已启动wegame请无视)", command=select_file)
    button_select_file.pack()


    # 创建确认按钮
    button_confirm = tk.Button(window, text="登录", command=lambda: get_token(game_combobox,account_combobox,zhmm,right_km,log_text,selected_wegame_file,window))
    button_confirm.pack()

    # 运行主循环
    window.mainloop()



def create_login_window():
    # 创建登录窗口
    login_window = tk.Tk()
    login_window.title("登录器")

    # 创建SSH服务器主机名的标签和输入框
    label_token = tk.Label(login_window, text="请输入登录卡密:")
    label_token.pack()
    entry_token = tk.Entry(login_window)
    entry_token.pack()

    # 创建日志文本框
    log_text = tk.Text(login_window, height=5)
    log_text.pack()

    # 创建确认按钮
    button_confirm = tk.Button(login_window, text="登录", command=lambda: login(entry_token,log_text,login_window))
    button_confirm.pack()

    # 运行主循环
    login_window.mainloop()



create_login_window()






































