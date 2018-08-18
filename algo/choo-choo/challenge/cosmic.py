#!/usr/bin/env python

import SocketServer
import time
import random
from num2words import num2words


HOST = "0.0.0.0"
PORT = 6052
FLAG = "flag{1_b3t_u_us3d_g00gle_tr4nslate}"


class connectionHandler(SocketServer.BaseRequestHandler):
    
    def handle(self):
        numIn = 4
        while numIn == 4:
            numIn = random.randint(0, 20)
            
        oldNum = numIn
        currNum = numIn

        orderList = [numIn]

        while (currNum != 4):
            currNum = len(num2words(oldNum))
            oldNum = currNum
            orderList.append(currNum)
            
        self.send("How do you get to infinity from " + str(numIn) + "? ")

        guess = recvall()
        guessSplit = guess.split(',')

        for i, element in enumerate(guessSplit):
            guessSplit[i] = int(element)
            
        if not guessSplit == orderList:
            outString = "No! I wanted "
            
            for i, element in enumerate(orderList):
                if not i == 0:
                    outString += ","
                outString += str(element)
                
            outString += "\nBecause\n"
            
            for i in range(1, len(orderList)):
                outString += str(orderList[i - 1]) + " is " + str(orderList[i]) + "\n"
            
            outString += "4 is infinity"

            self.send(outString)
        else:
            flag = "Ok, you seem to understand the mighty 4"
            flag += "flag{pr4is3_th3_c0smic_f0ur}"
            self.send(flag)

    def send(self, str):
        self.request.sendall(str)

    def recvall(self):
        s = self.request.recv(128)
        s.replace("\n", "")
        return s

def main():
    SocketServer.ForkingTCPServer.allow_reuse_address = True
    server = SocketServer.ForkingTCPServer((HOST, PORT), connectionHandler)
    server.serve_forever()

    print("Server started on port %s" %PORT)
    
if __name__ == "__main__":
    main()