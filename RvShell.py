import subprocess
import socket
import time
import os
import sys
from colorama import Fore,Back,Style
def Sleep():
    time.sleep(0.70)
def Commands(s,conn):
    print("[*]Instanziamento Comandi..")
    cmd=input("[#]Input..")
    '''if(cmd.startswith=="cd" ):
        print("[*]Navigazione nella directory..True..")
        os.chdir(cmd[3:])''' 


    if len(cmd)>0:
        conn.sendall(cmd.encode())
        data=s.recv(4096)
        data=data.decode("utf-8")
        print(data)
def Socket():
    try:
        print(Fore.RED+"[*]Creazione Socket")
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            Sleep()
            print(Style.RESET_ALL+"[*]Binding degli indirizzi..")
            s.bind((Ind,Port))

            Sleep()
            print("[*]Socket in ascolto..")
            s.listen()
            conn,addr=s.accept()
            Sleep()
            print("[*]Connessione ricevuta da ",addr)
            ''''data=conn.recv(4096)        
            data=data.decode("utf-8")'''
            Commands(s,conn)
    except KeyboardInterrupt as K:
        print(K)
    except Exception as errore:
        print(errore)
        sys.exit()
        sys.close()





if __name__=="__main__":
    Ind="127.0.0.1"
    Port=1025
    print("[*]Indirizzi bindati..",Ind,":",Port)
    Socket()