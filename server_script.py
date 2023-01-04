import socket

from server import tcp_streaming_server
#host_name=socket.gethostname()
#host_ip=socket.gethostbyname(host_name)
#print(host_ip)
server = tcp_streaming_server('127.0.0.1', 1024)
server.bind_socket()
server.listen()
server.serve()