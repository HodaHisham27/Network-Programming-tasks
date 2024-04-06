from socket import *

def recvall(sock):
    BUFF_SIZE = 1024
    data = ''
    while True:
        part = sock.recv(BUFF_SIZE)
        part = part.decode('utf-8')
        data += part
        if part[-1]=='\0':
            #sentinal at end of data
            break
    return data


try:
    s = socket(AF_INET,SOCK_STREAM)
    host = '127.0.0.1'
    port = 9000
    s.connect((host,port))
    
    while True:
        x = input("client: ")
        x+='\0'
        s.send(x.encode('utf-8'))
        y = recvall(s)
        print("server: ",y[:-1])
    
    conn.close()
except error as e:
    print(e)
except KeyboardInterrupt:
    pritn("ok!")