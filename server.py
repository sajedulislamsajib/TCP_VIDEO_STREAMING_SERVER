import socket
import pickle
import cv2
import struct
import threading


class tcp_streaming_server:
    def __init__(self, ip, port) -> None:
        # Write Initialization Code Here
        # self.socket = None
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket creation
        self.video_dim = (800, 600)

    def bind_socket(self) -> None:
        # Complete this

        self.socket.bind((self.ip, self.port))

    def listen(self) -> None:
        # Complete this
        self.socket.listen()
        print("Listening for connections.. ")

    def client_handler(self, client_socket) -> None:

        if client_socket is None:
            return
        path_to_video_file = "video.mp4"
        vid = cv2.VideoCapture(path_to_video_file)
        try:
            while vid.isOpened():
                _, frame = vid.read()
                frame = cv2.resize(frame, self.video_dim, fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
                a = pickle.dumps(frame)
                message = struct.pack("Q", len(a)) + a
                # Write Code to send Message
                client_socket.sendall(message)
                cv2.imshow('TRANSMITTING VIDEO', frame)
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    client_socket.close()
        except:
            None

    def serve(self) -> None:
        try:
            # Code for multithreaded service
            while True:
                # Accept incoming connections
                client_socket, client_address = self.socket.accept()
                print("Connected with " + client_address[0] + ' : ' + str(client_address[1]))
                # Start a new thread to handle the incoming connection
                client_thread = threading.Thread(target=self.client_handler, args=(client_socket,))
                client_thread.start()
        except KeyboardInterrupt:
            self.socket.close()