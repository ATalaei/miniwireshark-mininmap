import socket
import time
from scapy.all import *
# def mininmap_sender_tcpsockt(TCP_IP,TCP_PORT):
 
#  s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#  s.connect((TCP_IP,TCP_PORT))
#  s.close()

def synsender(target_ip,sport,dport):
    
     s_add="192.168.1.5"
     pkt=IP(src=s_add,dst=target_ip)/TCP(sport=sport,dport=dport,seq=1505066,flags="S")
     send(pkt)
      
      
       

 
 
 #if __name__ == "__main__":
def scanport(host,port):
     s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     #try:
     #s.connect((host,port))
     #s.bind(host,port+30000)
     print("Port open: "+str(port))
     s.close()
     #except:
     # print("Port closed: "+str(port)) 
 
TargetIPAdd=input("What is the target IP address? ")
   #rangenum=raw_input()
TargetPortNumberLow=input("Which ports do you want to scan? (LowerBound) ")
TargetPortNumberHigh= input("Which ports do you want to scan? (UpperBound) ")
   #rangenum=str(rangenum).split("-")
  # print(int(rangenum[0]),int(rangenum[1]))
for i in range(int(TargetPortNumberLow), int(TargetPortNumberHigh)):
  #  s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  #  s.connect((TargetIPAdd,i))
  #  s.send("")
  #  s.close()
  synsender(TargetIPAdd,i+2000,i)
  #scanport(TargetIPAdd,i)
  #mininmap_sender_tcpsockt(TargetIPAdd,i)
  #print("Sent TCP SYN packet to port"+str(i))
  #time.sleep(0.05) 