import socket               # Import socket module
import sys

text = "y"
while text == "y":
 s = socket.socket()         # Create a socket object
 host = socket.gethostname() # Get local machine name
 port = 12345                # Reserve a port for your service.
 s.bind((host, port))        # Bind to the port

 s.listen(5)                 # Now wait for client connection.
 print ('Server listening....')

 while True:

  c, addr = s.accept()     # Establish connection with client.
  print ('Got connection from', addr)
  msg1=c.recv(1024)
  msg1=msg1.decode('ascii')

  if msg1 == "exit":
   print ("Message received is: "+msg1+".Closing connection with this client. Open for further connections!!")
   #text = "bye from server"
   #c.send(text.encode('ascii'))
   #sys.exit()                            # Close the connection
   print("continue connection...")
   continue
  else:
   pmsg1= "Message received is: " + str(msg1)
   print (pmsg1)
   #text = input('Enter your message:')
   #c.send(text.encode('ascii'))
   #msgappend= "Echoed message: " + str(msg1)
   #c.send(msgappend.encode('ascii'))
   #msg2=c.recv(1024)
   #msg2=msg2.decode('ascii')
   #print(msg2)
   text=c.recv(1024)
   text=text.decode('ascii')
   if text == "n":
    #text = "bye from server"
    #c.send(text.encode('ascii'))
	#dmsg=c.recv(1024)
    #dmsg=dmsg.decode('ascii')
    print("Closing connection with this client. Open for further connections!!")
    #sys.exit()
   else:
    print("continue connection...")
    continue
