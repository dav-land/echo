import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.1.100', 10000)
print('Connecting to {} port {}'.format(server_address[0],server_address[1]),file=sys.stderr)
sock.connect(server_address)
try:
    
    # Send data
    message = 'This is the message.  It will be repeated.'
    print('sending "{}"'.format(message),file=sys.stderr)
    sock.sendall(message.encode())

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received "{}"'.format(data.decode()),file=sys.stderr)

finally:
    print('closing socket',file=sys.stderr)
    sock.close()
