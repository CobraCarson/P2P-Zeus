

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 999)
sock.connect(addr)
try: 
    message = 'true'
    sock.sendall(message.encode(encoding='utf_8'))
        
    data = sock.recv(300)
    print(data)
finally:
    print('closing socket')
    sock.close()