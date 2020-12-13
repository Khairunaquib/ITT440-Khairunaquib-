import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = "192.168.1.20"
port = 6000             # Reserve a port for your service.

s.connect((host, port))
print ("... Connected!\n")

filename = input(str("Enter file name : "))
file = open(filename,'rb')
data = file.read(1024)
s.send(data)

print("Done sending")
file.close()
s.close()
print("connection closed")
