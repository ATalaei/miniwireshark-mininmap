import binascii
import readline
from socket import inet_aton
from binascii import hexlify
from unittest import case
from miniwireshark import tcp
from chechsum3 import cs
import time
from pkt_sender import eth_sender



def ip2hex(ip):
  return " ".join(format(int(octet), "02x") for octet in str(ip).split("."))

def TcpSynSender(TargetIp,TargetPortNumber):

    fd=open('info.txt','r')
    Lines =fd.readlines()
    det_mac=Lines[6][:17]#.encode('utf-8')#destination mac
    src_mac =Lines[5][:17]#.encode('utf-8')#source mac
    ether_type="08 00"#ether_type
    ip_hdr_length="45"
    diff= "00" #different service
    t_len="00 3c"#total lenghth ("00 28" for 40 bytes ,"003c" for 60 bytes).
    id1="b7 cb"#id
    flags="40 00"#flages
    ttl="40"
    proto4="06"#layer 4 protocol number
    checksum_ip1="00 00"#ip check sum
    src_ip=ip2hex(Lines[2])#source ip
    dest_ip=ip2hex(TargetIp)#destination ip
    #For IP, the input is the hex stream of: ver,diff,t_len,id,flags,ttl,proto4,cs3,src_ip,dest_ip
    temp =ip_hdr_length+diff+t_len+id1+flags+ttl+proto4+checksum_ip1+src_ip+dest_ip
    temp=str(temp).replace(' ','')
    temp=" ".join(temp[i:i+2] for i in range (0,len(temp),2))
    checksum_ip1=cs(temp)
    src_port=Lines[3]
    src_port=src_port.strip()
    src_port=hex(int(src_port))   
    src_port=src_port[2:] 
    if(len(src_port)==1):
       src_port="0001"+src_port
    if(len(src_port)==2) :
        src_port="001"+src_port
    if(len(src_port)==3):
        src_port="01"+src_port
    dest_port=TargetPortNumber
    dest_port=hex(int(dest_port))   
    dest_port=dest_port[2:] 
    if(len(dest_port)==1):
        dest_port="000"+dest_port
    if(len(dest_port)==2) :
        dest_port="00"+dest_port
    if(len(dest_port)==3):
       dest_port="0"+dest_port
    seq_num="7f 5f 3c 85"#seq number
    ack="00 00 00 00"#ack number
    tcp_h_len="a0 02"#tcp header length and flags("a0 02" for 40 bytes, "50 02" for 20 bytes)
    window_size= " fa f0" #window size
    checksum_tcp="00 00" #tcp checksum
    urg_pointer ="00 00"#urgument pointer
    #For tcp, the input is the hex stream of: src_ip,dest_ip,"00",proto4,"00","14",src_port,dest_port,seq_num,
    # ack,h_len,w_size,"00 00",up
    temp=(src_ip+dest_ip+"00"+proto4+"00"+"28"+src_port+dest_port+seq_num+
    ack+tcp_h_len+window_size+"00 00"+urg_pointer+"02 04 05 b4 04 02 08 0a 10 50 9d 28 00 00 00 00 01 03 03 07")
    temp=str(temp).replace(' ','')
    temp=" ".join(temp[i:i+2] for i in range (0,len(temp),2))
    checksum_tcp=cs(temp)
    #print(checksum_tcp)
    interface0=Lines[4].strip()
    temp=(det_mac+src_mac+ether_type+ip_hdr_length+diff+t_len+id1+flags+
    ttl+proto4+checksum_ip1+src_ip+dest_ip+src_port+dest_port+seq_num+ack+
    tcp_h_len+window_size+checksum_tcp+urg_pointer+"02 04 05 b4 04 02 08 0a 10 50 9d 28 00 00 00 00 01 03 03 07")
    temp=str(temp).replace(' ','')
    temp=" ".join(temp[i:i+2] for i in range (0,len(temp),2))
    pkt=(temp)
    interface=Lines[4]
    interface=interface.strip()
    eth_sender(pkt,interface)
    

if __name__ == "__main__":
   TargetIPAdd=raw_input("What is the target IP address? ")
   #rangenum=raw_input()
   TargetPortNumberLow=input("Which ports do you want to scan? (LowerBound) ")
   TargetPortNumberHigh= input("Which ports do you want to scan? (UpperBound) ")
   #rangenum=str(rangenum).split("-")
  # print(int(rangenum[0]),int(rangenum[1]))
   for i in range(int(TargetPortNumberLow), int(TargetPortNumberHigh)):
    TcpSynSender(TargetIPAdd,i)
    print("Sent TCP SYN packet to port"+str(i))
    time.sleep(0.025)   
    
    
   
   
