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
    s= socket(AF_INET,SOCK_STREAM)
    host = '127.0.0.1'
    port = 9000
    s.bind((host,port))
    s.listen(5)
    
    print("Server is UP and listening")
    
    conn , addr = s.accept()
    print("recieved connection from: ",addr[0])
    
    while True:
        y = recvall(conn)
        print("client: ",y[:-1])
        x = input("server: ")
        x+='\0'
        conn.send(x.encode('utf-8'))
        
    conn.close()
    print("connection is closed")
    
except error as e:
    print(e)
except KeyboardInterrupt:
    print("ok!")
else :
    s.close()