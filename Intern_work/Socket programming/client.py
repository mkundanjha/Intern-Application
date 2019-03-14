import socket

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

host = socket.gethostname()

port = 8002

client.connect((host , port))

userDetails = str(input('userID'))+","+str(input('user password'))

client.send(userDetails.encode('ascii'))


output = client.recv(1024)
print(output.decode('ascii'))
