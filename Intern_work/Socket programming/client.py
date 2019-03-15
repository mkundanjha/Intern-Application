import socket

# Creating a socket object
client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

# Assigning host and port
host = socket.gethostname()
port = 8002

# Connecting to server
client.connect((host , port))

# Getting user details 
print("\nEnter the User-Id and Password for login\n")
userDetails = str(input('UserID: '))+","+str(input('Password: '))

# Sending data to the server
client.send(userDetails.encode('ascii'))

# Getting the output
output = client.recv(1024)
print(output.decode('ascii'))
