import socket
import termcolor

def target_communication():
    message =target.recv(1024)
    print (message)

sock =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 5555))
print(termcolor.colored('[***} LISTENING FOR INCOMING CONNECTIONS.....','green'))
sock.listen(5)

target, ip =sock.accept()
print(termcolor.colored('[***] Target connected from ' +str(ip),'green'))
target_communication()