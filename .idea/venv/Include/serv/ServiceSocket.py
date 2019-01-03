from socket import *
from time import ctime

# 1.定义域名和端口
HOST,PORT="",6666

# 2.定义缓冲区
BUFFER_SIZE=1024
ADDR=(HOST,PORT)

# 3创建服务器套接字
