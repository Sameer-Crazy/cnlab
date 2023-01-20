import socket
s = socket.socket()
s.bind(("",12345))
s.listen()
print("Server is listening....")
c,addr = s.accept()
print("Got a connection from ",addr)
c.send("Thank you for connecting!".encode())
c.send("index.html".encode())

