import re
from socket import inet_ntoa
from struct import *
import socket
import binascii

def ether(data):
    dest_mac,src_mac,proto_eth=unpack('! 6s 6s H',data[:14])
    dest_mac=':'.join(re.findall('..',dest_mac.encode('hex')))
    src_mac=':'.join(re.findall('..',src_mac.encode('hex')))
    return[dest_mac,src_mac,hex(proto_eth),data[14:]]

def ip(data):
    maindata=data
    data=unpack('! B s H 2s 2s B B 2s 4s 4s',data[:20])
    return [data[0]>>4,#version
    (data[0]&(0x0F))*4,#header lenghth
    "0x"+data[1].encode('hex'),#Diffserv
    data[2],#total length
    "0x"+data[3].encode('hex'),#ID
    "0x"+data[4].encode('hex'),#flag
    data[5],#ttl
    data[6],#protocol
    "0x"+data[7].encode('hex'),#checksum
    socket.inet_ntoa(data[8]),#source ip
    socket.inet_ntoa(data[9]),#destination ip
    #maindata[(data[0]&(0x0F))*4:]#ip payload
    maindata[(data[0]&(0x0F))*4:]]#ip payload
    
    
def tcp():
    conn=socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.ntohs(0x0003))
    raw_dat , add=conn.recvfrom(65535)
    ether_shark=ether(raw_dat) 
    
    if(ether_shark[2]=="0x800"):
         ip_shark=ip(ether_shark[3])
         if((int(ip_shark[7]))==6):
             tcp=ip_shark[11];
             tcp=unpack("!H H B B B B B B B B B B",tcp[:14])                 
             if(tcp[11]==18):
               print("Port "+str(tcp[0])+" is open on "+str(ip_shark[9]))
               return(ip_shark[9],tcp[0],tcp[1])
           
    return 0
           
if __name__ == "__main__":
    
  
  while True:
     x=(tcp())
     #if(x!=0):
      #   print(x)

