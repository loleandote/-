#!/usr/bin/python3 -u

import sys
import Ice
import os
import FileUploader
Ice.loadSlice('Frontend.ice')
import ServerSide


class FrontendI(ServerSide.Frontend):
    n = 0
    def write(self, message, current=None):
        print("{0}: {1}".format(self.n, message))
        sys.stdout.flush()
        self.n += 1
        return message
    def list(self, current=None):
        #sys.stdout.flush()
        return os.listdir('./')
    def prueba(self,baits, current=None):
        print(len(baits))
        sys.stdout.flush()
    def uploadFile(self, file, current=None):
        proxy = self.communicator().stringToProxy('FileManager -t -e 1.1:tcp -h 172.28.202.67 -p 7071 -t 60000')
        fileManager = ServerSide.FileManagerPrx.checkedCast(proxy)
        return fileManager.createUploader(file)

class Frontend(Ice.Application):
    def run(self, argv):
        broker = self.communicator()
        servant = FrontendI()

        adapter = broker.createObjectAdapter("FrontendAdapter")
        proxy = adapter.add(servant, broker.stringToIdentity("Frontend"))
        
        proxy2 = self.communicator().stringToProxy('FileManager -t -e 1.1:tcp -h 172.28.202.67 -p 7071 -t 60000')
        fileManager = ServerSide.FileManagerPrx.checkedCast(proxy2)
        fileManager.createUploader("hola")
        print(proxy, flush=True)

        adapter.activate()
        self.shutdownOnInterrupt()
        broker.waitForShutdown()

        return 0


frontend = Frontend()
sys.exit(frontend.main(sys.argv))
