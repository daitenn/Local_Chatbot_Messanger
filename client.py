import socket

M_SIZE = 1024

# Serverのアドレスを用意。Serverのアドレスは確認しておく必要がある。
serv_address = ('127.0.0.1', 8890)

# ①ソケットを作成する
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    try:
        # ②messageを送信する
        print('Input any messages, Type [end] to exit')
        message = input()
        if message != 'end':
            send_len = sock.sendto(message.encode('utf-8'), serv_address)
            # ※sendtoメソッドはkeyword arguments(address=serv_addressのような形式)を受け付けないので注意

            # ③Serverからのmessageを受付開始
            print('Waiting response from Server')
            rx_meesage, addr = sock.recvfrom(M_SIZE)
            print(f"[Server]: {rx_meesage.decode(encoding='utf-8')}")

        else:
            print('closing socket')
            sock.close()
            print('done')
            break

    except KeyboardInterrupt:
        print('closing socket')
        sock.close()
        print('done')
        break
