import socket
s = socket.socket()
s.connect(('127.0.0.1',12345))
print("Connection Established!")
while True:
    msg = input("Client: ")
    if(msg == "quit"):
        s.send(msg.encode())
        break
    else:
        s.send(msg.encode())
        reply = s.recv(1024)
        print("Server: ",reply.decode())
s.close()


