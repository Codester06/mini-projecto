import cv2
import socket
import numpy
import pickle

s=socket.socket(socket.AF_INET , socket.SOCK_DGRAM)  
ip="192.168.29.108"   
port=2323             
s.bind((ip,port)) 
while True:
    x=s.recvfrom(100000000)    # Recieve byte code sent by client using recvfrom
    clientip = x[1][0]         # x[1][0] in this client details stored,x[0][0] Client message Stored
    data=x[0]                  # Data sent by client
    data=pickle.loads(data)    # All byte code is converted to Numpy Code 
    data = cv2.imdecode(data, cv2.IMREAD_COLOR)  # Decode 
    cv2.imshow('sender', data) # Show Video/Stream
    if cv2.waitKey(10) == 13:  # Press Enter then window will close
        break
cv2.destroyAllWindows()   