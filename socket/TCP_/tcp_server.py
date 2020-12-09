import  socket
def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(("", 8090))
    tcp_server_socket.listen(128)
    while True:
        print("等待一个新的客户到来...")
        new_client_socket, client_addr = tcp_server_socket.accept()
        print("一个新的客户已经到来:%s" % str(client_addr))
        while True:
            recv_data = new_client_socket.recv(1024)
            print("客户发送过来的请求:%s" % recv_data.decode("gbk"))
            if recv_data:
                new_client_socket.send("我已经收到你的请求".encode("gbk"))
            else:
                break;

        new_client_socket.close()
        print("已经为客户端服务完毕")
    #tcp_server_socket.close()

if __name__ == '__main__':
    main()
