#!/usr/bin/python3 -u

import sys
import Ice
import os
import Uploader
Ice.loadSlice('urfs.ice')
import URFS


class FrontendI(URFS.Frontend):
    def __init__(self, fileManager):
            self.fileManager = fileManager
    def getFileList(self, current=None):
        archivos=os.listdir('./')
        lista=[]
        for archivo in archivos:
            lista.append(URFS.FileInfo(archivo,archivo))
        return lista
    def uploadFile(self, file, current=None):
        return self.fileManager.createUploader(file)
    def downloadFile(self, file, current=None):
         return self.fileManager.createDownloader(file)

class Frontend(Ice.Application):
    def run(self, argv):
        broker = self.communicator()
        
        #proxy = self.communicator().stringToProxy('FileManager -t -e 1.1:tcp -h 172.28.202.67 -p 7071 -t 60000')
        proxy = self.communicator().stringToProxy('FileManager -t -e 1.1:tcp -h 172.25.72.183 -p 7071 -t 60000')
        fileManager = URFS.FileManagerPrx.checkedCast(proxy)
        servant = FrontendI(fileManager)
        #servant = FrontendI()
        adapter = broker.createObjectAdapter("FrontendAdapter")
        proxy = adapter.add(servant, broker.stringToIdentity("Frontend"))
        print(proxy, flush=True)

        adapter.activate()
        self.shutdownOnInterrupt()
        broker.waitForShutdown()

        return 0
frontend = Frontend()
sys.exit(frontend.main(sys.argv))
