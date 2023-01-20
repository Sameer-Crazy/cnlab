import socket
s = socket.socket()
s.connect(("127.0.0.1",12345))
print("Connection Established!")
filename = input("Enter the filename: ")
s.send(filename.encode())
f = open(("Downloaded "+filename),'wb')
data = s.recv(1024)
while data:
    f.write(data)
    data = s.recv(1024)
print("Transfer Complete!")
s.close()