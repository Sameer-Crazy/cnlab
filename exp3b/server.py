import socket
s = socket.socket()
s.bind(('127.0.0.1',12345))
s.listen()
print("Server is listening...")
c,addr = s.accept()
username = c.recv(1024).decode()
print("Got a connection from ",username,addr)
while True:
    msg = c.recv(1024).decode()
    if msg!="quit":
        print(username,": ",msg)
        reply = input("You: ")
        c.send(reply.encode())
    else:
        c.close()
        break
s.close()


