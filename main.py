#leighTrinity
#

import socket
import termcolor


s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((b'127.0.0.1', 5555))
message =b"hello world"
s.send(message)