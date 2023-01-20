import socket
def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append("0")
        else:
            result.append("1")
    return "".join(result)
def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[0:pick]
    while pick < len(dividend):
        if tmp[0] == "1":
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor("0" * pick, tmp) + dividend[pick]
        pick += 1
    if tmp[0] == "1":
        tmp = xor(divisor, tmp)
    else:
        tmp = xor("0" * pick, tmp)
    checkword = tmp
    return checkword
def decodeData(data, key):
    l_key = len(key)
    appended_data = data + "0" * (l_key - 1)
    remainder = mod2div(appended_data, key)
    return remainder

s = socket.socket()
port = 12345
s.bind(("127.0.0.1", port))
s.listen()
print("Server is listening...")
while True:
    c, addr = s.accept()
    print("Got connection from ", addr)
    data = c.recv(1024).decode()
    print("Received encoded data in Binary format:", data)
    if not data:
        break
    key = "1001"
    ans = decodeData(data, key)
    print("Data after decoding is: ", ans)
    temp = "0" * (len(key) - 1)
    if ans == temp:
        c.sendto(("Thank you, Data " + data + " has been received and NO ERROR FOUND").encode(),("127.0.0.1", 12345))
    else:
        c.sendto(("Error in Data!").encode(), ("127.0.0.1", 12345))
    c.close()
s.close()