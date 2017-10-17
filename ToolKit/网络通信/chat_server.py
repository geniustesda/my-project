# -*- coding:utf-8 -*-
import socket
import threading
from time import ctime, sleep
socks = []
users_id = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 19998))
s.listen(5)  # 监听5个用户
print("等待客户端连接...")  # 此处必须继承link中的user_id,不然会导致user_id在两者通信时始终不变，从而起不到监听作用


def send(data, aim_id, user_id):
    context = user_id.decode('utf-8')+"跟你说："+data.decode('utf-8')+"---"+ctime()
    socks[users_id.index(aim_id)].send(context.encode('utf-8'))
    # 监听客户端的通信
    print(user_id.decode('utf-8')+"跟"+aim_id.decode('utf-8')+"说："+data.decode('utf-8')+"---"+ctime())


def add(content, user_id):
    for u in users_id:
        string = user_id.decode('utf-8')+"发布了一条公告："+content.decode('utf-8')+"---"+ctime()
        socks[users_id.index(u)].send(string.encode('utf-8'))
    # 监听客户端的公告
    print(user_id.decode('utf-8')+"发布了一条公告："+content.decode('utf-8')+"---"+ctime())


def online(user_id, sock):
    string=""
    for u in users_id:
        num = users_id.index(u)
        string += str(num+1)+"."+u.decode('utf-8')+"\n"
    sock.send(string.encode('utf-8'))
    print(user_id.decode('utf-8')+"请求了在线人员名单"+"---"+ctime())


def link(sock, addr):
    global socks, users_id
    user_id = sock.recv(1024)
    users_id = users_id+[user_id]
    socks = socks+[sock]
    sock.send("当前在线人员：\n".encode('utf-8'))
    online(user_id, sock)
    print(user_id.decode('utf-8')+"已连接！"+"---"+ctime())
    try:
        while True:
            order = sock.recv(1024)
            if(order.decode('utf-8') == "exit"):
                print(user_id.decode('utf-8')+"已退出连接！"+"---"+ctime())
                break
            elif(order.decode('utf-8') == "send"):
                aim_id = sock.recv(1024)
                data = sock.recv(1024)
                send(data, aim_id, user_id)
            elif(order.decode('utf-8') == "add"):
                content = sock.recv(1024)
                add(content, user_id)
            elif(order.decode('utf-8') == "online"):
                online(user_id, sock)
            else:
                sock.send("无该命令！".encode('utf-8'))
                continue
    except :
        print(user_id.decode('utf-8')+"已断开！"+"---"+ctime())
        users_id.remove(user_id)
while True:
    sock, addr = s.accept()
    t = threading.Thread(target=link, args=(sock, addr))
    t.start()