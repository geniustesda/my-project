# -*- coding:utf-8 -*-
import socket
import threading
import sys
from time import sleep

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect(('127.0.0.1', 19998))
    print("请输入你的ID")
    user_id = input()
    s.send(user_id.encode('utf-8'))
    print("send:发送消息")
    print("add:发送一条公告")
    print("exit:退出")
    print("online:显示当前在线的人")
except:
    print("连接服务器失败")
    sys.exit(0)


# 监听服务端
def listen(x):
    while True:
        print(s.recv(1024).decode('utf-8'))


t = threading.Thread(target=listen, args=(10,))
t.start()

while True:
    sleep(0.1)
    print("\n输入你的命令：")
    order = input()
    s.send(order.encode('utf-8'))
    if (order == "exit"):
        print("聊天结束！程序将在5秒后退出...")
        sleep(5)
        break
    if (order == "send"):
        print("接收者ID")
        aim_id = input()
        s.send(aim_id.encode('utf-8'))
        print('消息内容：')
        data = input()
        s.send(data.encode('utf-8'))
        print("发送成功！")
    if (order == "add"):
        print("请输入公告内容：")
        content = input()
        s.send(content.encode('utf-8'))

print("退出中...")
sleep(1)
s.close()