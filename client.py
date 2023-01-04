import pickle
import socket
import struct
import cv2


class client:
    def __init__(self, server_ip, server_port) -> None:
        # Initilization code

        self.server_ip = server_ip
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket creation

    def connect_to_server(self) -> None:
        # Code to connect to server

        self.client_socket.connect((self.server_ip, self.server_port))

    def receive_video_data(self) -> None:
        data = b""
        try:
            payload_size = struct.calcsize("Q")

            while True:

                # Code to receive messages chunk by chunk
                # and constitute them into full messsage
                while len(data) < payload_size:
                    packet = self.client_socket.recv(4 * 1024)
                    if not packet: break
                    data += packet
                packed_msg_size = data[:payload_size]
                data = data[payload_size:]

                msg_size = struct.unpack("Q", packed_msg_size)[0]
                # print(msg_size)
                while len(data) < msg_size:
                    data += self.client_socket.recv(4 * 1024)
                frame_data = data[:msg_size]
                data = data[msg_size:]
                frame = pickle.loads(frame_data)
                cv2.imshow("RECEIVING VIDEO", frame)
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    break

            self.client_socket.close()
        except KeyboardInterrupt:
            self.client_socket.close()

