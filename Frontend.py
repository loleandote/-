#!/usr/bin/python3 -u

import sys
import Ice
import os
import Uploader
Ice.loadSlice('urfs.ice')
import URFS


class FrontendI(URFS.Frontend):
    # def uploadFile(self, file, current=None):
    #     proxy = self.communicator().stringToProxy('FileManager -t -e 1.1:tcp -h 172.28.202.67 -p 7071 -t 60000')
    #     fileManager = URFS.FileManagerPrx.checkedCast(proxy)
    #     return fileManager.createUploader(file)
    def getFileList(self, current=None):
        #sys.stdout.flush()
        archivos=os.listdir('./')
        lista=[]
        for archivo in archivos:
            lista.append(URFS.FileInfo(archivo,archivo))
        return lista
    def prueba(self,baits, current=None):
        print(len(baits))
        sys.stdout.flush()
    

class Frontend(Ice.Application):
    def run(self, argv):
        broker = self.communicator()
        servant = FrontendI()

        adapter = broker.createObjectAdapter("FrontendAdapter")
        proxy = adapter.add(servant, broker.stringToIdentity("Frontend"))
        
        proxy2 = self.communicator().stringToProxy('FileManager -t -e 1.1:tcp -h 172.28.202.67 -p 7071 -t 60000')
        fileManager = URFS.FileManagerPrx.checkedCast(proxy2)
        fileManager.createUploader("hola")
        print(proxy, flush=True)

        adapter.activate()
        self.shutdownOnInterrupt()
        broker.waitForShutdown()

        return 0


frontend = Frontend()
sys.exit(frontend.main(sys.argv))
