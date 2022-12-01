import socket
s=socket.socket()
s.bind(("localhost",9999))
s.listen(5)
print("Waiting for connection")
c,a=s.accept()
while True:
    
    data=c.recv(1024).decode()
    #print("Connected with",addr)
    print("MR C:",data,"\n")
    if(data=="bye"):
        c.send(bytes("bye",'utf-8'))
        print("end")
        c.close()
        break

    msg=input("ENTER MSG")
    c.send(bytes(msg,"utf-8"))
    
    

