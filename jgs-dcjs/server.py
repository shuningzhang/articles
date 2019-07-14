#!/usr/bin/env python3
#-*- coding:utf-8 -*-
from socket import *
from time import ctime
host = ''
port = 12345
buffsize = 2048
ADDR = (host,port)
# 创建一个基于TCP协议的套接字
tctime = socket(AF_INET,SOCK_STREAM)
tctime.bind(ADDR)
# 在指定的地址和端口监听
tctime.listen(3)
while True:
    print('Wait for connection ...')
    tctimeClient,addr = tctime.accept()
    print("Connection from :",addr)
    while True:
        data = tctimeClient.recv(buffsize).decode()
        if not data:
            break
        tctimeClient.send(('[%s] %s' % (ctime(),data)).encode())
tctimeClient.close()
tctime.close()
