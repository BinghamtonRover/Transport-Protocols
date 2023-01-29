import socket
import cv2
import imutils
import time
import base64
import numpy as np

cv2.destroyAllWindows()

localIP     = "127.0.0.1"
localPort   = 9002
bufferSize  = 65536

msgFromServer       = "Hello UDP Client"
bytesToSend         = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
UDPServerSocket.settimeout(0.5)

print("UDP server up and listening")

#cap = cv2.VideoCapture(0)





#cap.release()

# Closes all the frames
#cv2.destroyAllWindows()



# Listen for incoming datagrams
try:
    while(True):
        try:
            bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
            #message = bytesAddressPair[0]
            #address = bytesAddressPair[1]
            #clientMsg = "{}".format(message)
            #clientIP  = "Client IP Address:{}".format(address)

            #print("frame recieved:")
            #print("bytesAddressPair:")
            #print(bytesAddressPair)
            #print(type(bytesAddressPair[0]))
            data = np.frombuffer(bytesAddressPair[0], np.uint8)
            #data = base64.b64decode(bytesAddressPair, '/')
            #npdata = np.fromstring(data,dtype=np.uint8)
            fixedMsgframe = cv2.imdecode(data,1)

            #im = Image.new()
            #im.load_jpg_from_buffer(clientMsg)
            #im_tx = ImageTexture.new()
            #im_tx.create_from_image(im)

            #print(fixedMsg)
            cv2.imshow('Frame',fixedMsgframe)

            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                print("INSIDE");
                break


            #print(clientMsg)
            #print(clientIP)

		    # Sending a reply to client
            #qUDPServerSocket.sendto(bytesToSend, address)

        except socket.timeout: pass
except KeyboardInterrupt:
	print("Closing server")

cv2.destroyAllWindows()
UDPServerSocket.close()
