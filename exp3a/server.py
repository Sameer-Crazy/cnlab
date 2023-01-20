import socket
s = socket.socket()
s.bind(('127.0.0.1',12345))
s.listen()
print("Server is Listening....")
c,addr = s.accept()
print("Got a connection from ",addr)
while True:
    msg = c.recv(1024).decode()
    if msg!="quit":
        c.send(msg.encode())
    else:
        c.close()
        break
s.close()
    
