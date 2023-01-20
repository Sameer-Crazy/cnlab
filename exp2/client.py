import socket
import webbrowser
s = socket.socket()
s.connect(("127.0.0.1",12345))
print(s.recv(1024).decode())
file = s.recv(1024).decode()
webbrowser.open_new_tab(file)
s.close()