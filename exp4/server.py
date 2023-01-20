import socket
dns_table = {
    "www.google.com":"142.250.183.68",
    "www.youtube.com":"142.251.42.78",
    "www.netflix.com":"54.73.148.110",
    "54.73.148.110":"www.netflix.com",
    "142.251.42.78":"www.youtube.com",
    "142.250.183.68":"www.google.com"
}
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("127.0.0.1",12345))
print("Server Started...")
while True:
    data,addr = s.recvfrom(1024)
    print(f"{addr} wants to fetch the data!")
    data = data.decode()
    ip = dns_table.get(data,"Not Found").encode()
    s.sendto(ip,addr)
    reply,addr = s.recvfrom(1024)
    if reply.decode() == 'n':
        break
s.close()