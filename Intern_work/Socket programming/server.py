import socket

#Creating a Socket Object
serverSocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

# Assigning Host and Port number
host = socket.gethostname()
port = 8002

# Making Server listen for incoming client requests
serverSocket.bind((host , port))
serverSocket.listen(5)

# This is a dictionary of User_id: Password format
userId = {'mkundanjha' : 'kundan123' , 'imjack' : 'jack24#'}

while True:
	clientSocket , details = serverSocket.accept()
	print(details)
	print("Connection Established with client.")
	userDetails = clientSocket.recv(1024).decode('ascii').split(',')
	if userDetails[0] in userId:
		if userId[userDetails[0]] == userDetails[1]:
			clientSocket.send(("Authorization Sucessful. You are logged in.").encode('ascii'))
		else:
			clientSocket.send(("Acess Denied. You are not a valid user.").encode('ascii'))
	else:
		clientSocket.send(("Acess Denied. You are not a valid user.").encode('ascii'))

