import socket
import sys

#create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the socket to the port
server_address = ('192.168.1.100', 10000)
print('starting up on {} port {}'.format(server_address[0], server_address[1]), file=sys.stderr)
sock.bind(server_address)

#Listen for incoming connections
sock.listen(1)

while True:
    #wait for a connection
    print('waiting for a connection',file=sys.stderr)
    connection, client_address = sock.accept()
    try:
        print('connection from {}'.format(client_address), file=sys.stderr)
        
        #recieve the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print('recieved "{}"'.format(data), file=sys.stderr)
            if data:
                print('sending data back to the client',file=sys.stderr)
                connection.sendall(data)
            else:
                print('no more data from {}'.format(client_address), file=sys.stderr)
                break

    finally:
        #clean up the connection
        connection.close()
