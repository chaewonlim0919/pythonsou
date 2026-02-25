# socket : 소켓(Socket)은 프로세스가 네트워크 세계로 데이터를 내보내거나 혹은 그 세계로부터 데이터를 받기 위한 실제적인 창구 역할을 한다.
# 그러므로 프로세스가 데이터를 보내거나 받기 위해서는 반드시 소켓을 열어서  소켓으로부터 데이터를 읽어들여야 한다.
# socket이란 TCP/IP의 프로그래머 인터페이스이다.
# 통신 기기간 대화가 가능하도록 하는 통신방식으로 클라이언트/서버 모델에 기초한다.
# 연결지향: TCP/IP
# 비연결지향: UDP

# socket 통신 확인
import socket

print(socket.getservbyname('http', 'tcp'))
print(socket.getservbyname('ssh', 'tcp'))
print(socket.getservbyname('ftp', 'tcp'))
print(socket.getservbyname('smtp', 'tcp'))
print(socket.getservbyname('pop3', 'tcp'))