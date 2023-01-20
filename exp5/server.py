import socket
table = {
    '192.168.1.1': '1E.4A.4A.11',
    '192.168.2.1': '5E.51.4B.01',
    '192.168.1.3': '4B.35.CD.32',
    '4B.35.CD.32': '192.168.1.3',
    '5E.51.4B.01': '192.168.2.1',
    '1E.4A.4A.11': '192.168.1.1'
}
s = socket.socket()
ip = '127.0.0.1'
s.bind((ip, 1234))
s.listen()
print("Socket is listening...")
clientsocket, adrress = s.accept()
ip = clientsocket.recv(1024)
ip = ip.decode('utf-8')
mac = table.get(ip, "no entry for given address")
clientsocket.send(mac.encode())
