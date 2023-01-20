import socket
s = socket.socket()
username = input("What is your name: ")
s.connect(('127.0.0.1',12345))
s.send(username.encode())
print("Connection Established!")
print("--------------------------------")
while True:
    msg = input("You: ")
    if (msg!="quit"):
        s.send(msg.encode())
        reply = s.recv(1024).decode()
        print("Server: ",reply)
    else:
        s.send(msg.encode())
        break
s.close()