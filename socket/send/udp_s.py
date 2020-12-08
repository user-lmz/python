import socket

def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("", 8089))
    dest_ip = input("请输入对方ip:")
    dest_port = int(input("请输入对方port:"))
    while True:
        send_data = input("请输入要发送的数据：")
        if send_data == "end":
            break
        udp_socket.sendto(send_data.encode('gbk'), (dest_ip, dest_port))
    udp_socket.close()

if __name__ == '__main__':
    main()