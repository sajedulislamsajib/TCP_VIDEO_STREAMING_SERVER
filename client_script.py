from client import client
#import socket
#host = socket.gethostname()
#print(host)
#client = client(host, 9999)
client = client('127.0.0.1', 1024)
client.connect_to_server()
client.receive_video_data()
