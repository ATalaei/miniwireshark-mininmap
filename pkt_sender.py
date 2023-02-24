import math
#from pyexpat.errors import messages
import socket
from sqlite3 import InterfaceError
import string
import binascii 
#from mailbox import linesep
# s = socket.socket(socket.AF_PACKET,socket.SOCK_RAW)

# print ("What is your packet content? ", end='')
# string_payload= (input())
# pkt=binascii.unhexlify(string_payload)
# print ("Which interface do you want to use? ",end='' )
# InterfaceVar=input()
# s.bind((InterfaceVar, 0))
# if(string_payload!=""):
#    res = bin(int(string_payload, 16))
#    string_payload = res[2:]
#    payloadvar=(string_payload)
#    res = bytes(payloadvar, 'utf-8')
#    payload=res
   


# src_addr = "\x12\x34\x56\x78\x09\x12"
# src_addr = bytes(src_addr, 'utf-8')

# dst_addr = "\x01\x02\x03\x04\x05\x06"
# dst_addr = bytes(dst_addr, 'utf-8')

# checksum = "\x01\x02\x03\x04"
# checksum = bytes(checksum, 'utf-8')
# ethertype = "\x08\x00"
# ethertype = bytes(ethertype, 'utf-8')
# if string_payload!="":
 
#   #s.send(dst_addr+src_addr+ethertype+payload)
#    s.send (pkt)
# else: 
#    s.send(dst_addr+src_addr+ethertype)

#print("Sent "+str(math.ceil(len(pkt)))+"-byte packet on",InterfaceVar)

def eth_sender(message,interface) :
    
    message=str(message).replace(' ','')
    messagelength=len(message)
    if((len(message)%2)!=0):
        message=str(message)+"0"
        
    pkt = binascii.unhexlify(str(message))
    s=socket.socket(socket.AF_PACKET,socket.SOCK_RAW)
    s.bind((interface,0))
    s.send(pkt)
    s.close()
    #return("Sent" +str(int(messagelength/2))+"-byte packet on " +str(interface))
    print("Sent" +str(int(messagelength/2))+"-byte packet on " +str(interface))

if __name__ == "__main__":
   message=input("What is your packet content? ")
   Interface=raw_input("Which interface do you want to use? ")
   eth_sender(message,Interface)
   
