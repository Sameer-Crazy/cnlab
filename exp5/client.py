import socket
s = socket.socket()
ip = '127.0.0.1'
s.connect((ip, 1234))
a = input('ARP or RARP : ')
if (a == "ARP"):
    add = input("enter ip : ")
elif (a == "RARP"):
    add = input("enter MAC : ")
s.send(add.encode())
mac = s.recv(1024)
mac = mac.decode("utf-8")
if (a == "ARP"):
    print("MAC of", add, 'is : ', mac)
else:
    print('IP of ',add, 'is : ', mac)
