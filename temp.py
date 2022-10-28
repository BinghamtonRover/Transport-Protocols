"""
A quick script to print out any data received over UDP

We're actually sending Protobuf messages but this script is just to verify 
that data was received on the right IP address and port. Save the processing
for the actual C++ code.
"""

import socket

localIP     = "127.0.0.1"
localPort   = 8082
bufferSize  = 1024

# Create a datagram socket
udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
udp.bind((localIP, localPort))
udp.settimeout(0.5)
print("UDP server up and listening")

def close(): 
	print("Shutting down server")
	udp.close()
	print("Done")
	quit()

# Listen for incoming datagrams
try: 
	while(True):
		try: 
		  message, address = udp.recvfrom(bufferSize)
		  print(f"Message from Client: {message}")
		  print(f"Client IP Address: {address}")
		except socket.timeout: pass
		except KeyboardInterrupt: close()
except KeyboardInterrupt: close()
