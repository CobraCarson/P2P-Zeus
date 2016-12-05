import socket, random

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 999)
sock.bind(addr)

sock.listen(1)
  
def store_data(addr, port):
    filename = open('addr.txt', 'a')
    filer = open('addr.txt')
    port = str(port)
    file_contents = filer.read()
    if addr in file_contents:
        ''' edit this to seperate node from worker '''
    else:
        filename.write(addr + ' ' + port + '\n') 
       
def getNode():
    file = open('addr.txt', 'r')
    file = file.readlines()
    print(file[0])

while True: 
    connection, client_addr = sock.accept()
    try:
        while True:
            data = connection.recv(300)
            if data:
                store_data(client_addr[0], client_addr[1])
                '''
                    Create function to pick a random node ip and connect to it.
                '''

                sock.sendall()
            else:
                break
            
    finally:
        # Clean up the connection
        connection.close()
        
