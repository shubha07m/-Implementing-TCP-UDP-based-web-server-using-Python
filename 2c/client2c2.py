import socket

HOST =socket.gethostname()
PORT = 8888           
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(("172.17.2.15",PORT))

text=input('Enter your mesage:') #take message input from user
socket.send(text.encode('ascii'))     #send message to client

#socket.close()