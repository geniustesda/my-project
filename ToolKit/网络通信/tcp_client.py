# -*- coding:utf-8 -*-
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
for i in range(100):
    for data in [b'Michael', b'Tracy', b'Sarah',]:
        # 发送数据:
        s.send(data)
        print(s.recv(1024).decode('utf-8'))
    import time
    time.sleep(1)
    print("第%d次会话结束" % int(i+1))
s.send(b'exit')
s.close()
