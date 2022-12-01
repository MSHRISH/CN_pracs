import socket

c=socket.socket()

c.connect(("localhost",9999))




while True:
    msg=input("Enter your Message: ")
    c.send(bytes(msg,"utf-8"))
    recvd=c.recv(1024).decode()
    print("MR S: ",recvd)   