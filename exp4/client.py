import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
address = ("127.0.0.1",12345)
while True:
    req_domain = input("Enter the domain: ")
    s.sendto(req_domain.encode(),address)
    data,addr = s.recvfrom(1024)
    print(data)
    print(f"IP Address of {req_domain} is: {data.decode()}")
    c = input("Do u want to continue? (Y/N): ").lower()
    s.sendto(c.encode(),address)
    if c=='n':
        break
s.close()
