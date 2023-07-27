from socket import *

def local2nex( clientSock, filename ):
    while (1):
        # Receive file existence status from the server
        data = clientSock.recv(1024)
        print('hello1')
        if not data:
            print('파일 %s 가 서버에 존재하지 않음' % filename)
            continue

        nowdir = os.getcwd()
        with open(os.path.join(nowdir, filename), 'wb') as f:
            data_transferred = 0
            data_transferred2 = 0
            print('hello2')
            # Receive and write file data
            try:
                while True:
                    data = clientSock.recv(1024)
                    if not data:
                        break
                    f.write(data)
                    data_transferred += len(data)
                    if len(data) == 0 :
                        print('len_break')
                        break
                    elif data_transferred % 1024 != 0 :
                        print('1024_break')
                        break
                print('파일 %s 받기 완료. 전송량 %d' % (filename, data_transferred))
                data_transferred = 0
            except Exception as ex:
                print(ex)
