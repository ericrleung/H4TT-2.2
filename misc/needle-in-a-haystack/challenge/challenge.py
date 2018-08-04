#!/usr/bin/env python

import SocketServer
import time
import random

HOST = "0.0.0.0"
PORT = 6050
FLAG = "flag{1_b3t_u_us3d_g00gle_tr4nslate}"


class connectionHandler(SocketServer.BaseRequestHandler):
    
    def handle(self):
        handle = open('/dev/urandom')
        offset = random.randint(15,60)
        starting_time = int(time.time())

        while(True):
            if(int(time.time()) != starting_time + offset):
                garbage = handle.read(1)
                self.send(garbage)
            else:
                self.send(FLAG)
                starting_time = time.time()
                offset = random.randint(60,120)

    def send(self, str):
        self.request.sendall(str)

def main():
    SocketServer.ForkingTCPServer.allow_reuse_address = True
    server = SocketServer.ForkingTCPServer((HOST, PORT), connectionHandler)
    server.serve_forever()

    print("Server started on port %s" %PORT)
    
if __name__ == "__main__":
    main()