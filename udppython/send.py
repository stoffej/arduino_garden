import socket
 
UDP_IP = "192.168.1.20"
UDP_PORT = 8888
MESSAGE = "Hello from pc"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet 
		      socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
