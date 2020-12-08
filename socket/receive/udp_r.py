import socket

def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    localaddr = ('', 7878)
    udp_socket.bind(localaddr)
    while True:
        recv_data = udp_socket.recvfrom(1024)
        recv_msg = recv_data[0]
        send_addr = recv_data[1]
        if recv_msg.decode("gbk") == "exit":
            break
        print("address:%s, message:%s"%(str(send_addr), recv_msg.decode("gbk")))
    udp_socket.close()

if __name__ == "__main__":
    main()