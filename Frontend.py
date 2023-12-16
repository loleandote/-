#!/usr/bin/python3 -u

import sys
import Ice
import os
import Uploader
Ice.loadSlice('urfs.ice')
import URFS


class FrontendI(ServerSide.Frontend):
    n = 0
    def __init__(self, fileManager):
            self.fileManager = fileManager
    def write(self, message, current=None):
        print("{0}: {1}".format(self.n, message))
        sys.stdout.flush()
        self.n += 1
        return message
    def list(self, current=None):
        #sys.stdout.flush()
        archivos=os.listdir('./')
        lista=[]
        for archivo in archivos:
            lista.append(URFS.FileInfo(archivo,archivo))
        return lista
    def prueba(self,baits, current=None):
        print(len(baits))
        sys.stdout.flush()
    def uploadFile(self, file, current=None):
        
        return self.fileManager.createUploader(file)
    def downloadFile(self, file, current=None):
         return self.fileManager.createDownloader(file)

class Frontend(Ice.Application):
    def run(self, argv):
        broker = self.communicator()
        
        proxy = self.communicator().stringToProxy('FileManager -t -e 1.1:tcp -h 172.28.202.67 -p 7071 -t 60000')
        fileManager = ServerSide.FileManagerPrx.checkedCast(proxy)
        servant = FrontendI(fileManager)

        adapter = broker.createObjectAdapter("FrontendAdapter")
        proxy = adapter.add(servant, broker.stringToIdentity("Frontend"))
        print(proxy, flush=True)

        adapter.activate()
        self.shutdownOnInterrupt()
        broker.waitForShutdown()

        return 0
frontend = Frontend()
sys.exit(frontend.main(sys.argv))
