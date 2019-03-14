import socket


serverSocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

host = socket.gethostname()

port = 8002

serverSocket.bind((host , port))

serverSocket.listen(5)

userId = {'lazycoderr' : 'arpit' , 'momo' : 'kundan'}

while True:
	clientSocket , details = serverSocket.accept()
	print(details)
	userDetails = clientSocket.recv(1024).decode('ascii').split(',')
	if userDetails[0] in userId:
		if userId[userDetails[0]] == userDetails[1]:
			clientSocket.send(("data is present").encode('ascii'))
		else:
			clientSocket.send(("data is not present").encode('ascii'))
	else:
		clientSocket.send(("data is not present").encode('ascii'))

