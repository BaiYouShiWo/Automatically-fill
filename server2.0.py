import socket
from threading import Thread
import traceback
import winsound
import pygame
import time

HOST = "192.168.2.5"
PORT = 65432
def recv_from_client(conn):
    try:
        content = conn.recv(1024)
        return content
    except Exception:
        return None

class ServiceThread(Thread):
    def __init__(self, conn, addr):
        super().__init__()
        self.conn = conn
        self.addr = addr

    def run(self):
        try:
            while True:
                content = recv_from_client(self.conn)
                if not content:
                    break
                print(f"{self.addr}: {content.decode('utf-8')}")

                self.conn.sendall(content)
            self.conn.close()
            print(f"{self.addr[0]}:{self.addr[1]} leave.")
        except Exception:
            traceback.print_exc()

if __name__ == "__main__":
    flag=0
    s = None
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen()
        print("Repeater server started successfully.")
        while True:
            flag+=1
            conn, addr = s.accept()
            print(f"Connected from {addr}")
            if flag==1:
                filepath = r"H:\CloudMusic\Wolfgang Amadeus Mozart - 小星星变奏曲.mp3"
                pygame.mixer.init()
                pygame.mixer.music.load(filepath)
                pygame.mixer.music.play(start=0.0)
                time.sleep(20)
            elif flag%2==0:
                pygame.mixer.music.pause() #暂停
            elif flag>1 and flag%2==1:
                pygame.mixer.music.unpause()#取消暂停
            service_thread = ServiceThread(conn, addr)
            service_thread.daemon = True
            service_thread.start()
    except Exception:
        traceback.print_exc()
    s.close()