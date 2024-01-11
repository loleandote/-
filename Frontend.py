#!/usr/bin/python3 -u

import sys
import Ice
import os
import Uploader
Ice.loadSlice('urfs.ice')
import URFS
import IceStorm
from FrontendUpdates import FrontendUpdatesI

class FrontendI(URFS.Frontend):
    def __init__(self, fileManager):
            self.fileManager = fileManager
            self.filelist=[]
    def getFileList(self, current=None):
        archivos=os.listdir('./')
        lista=[]
        print("hoas")
        print(len(self.filelist))
        for archivo in self.filelist:
             print(archivo)
        for archivo in archivos:
            lista.append(URFS.FileInfo(archivo,archivo))
        return self.filelist
    def uploadFile(self, file, current=None):
        return self.fileManager.createUploader(file)
    def downloadFile(self, file, current=None):
         return self.fileManager.createDownloader(file)
    def removeFile(self, file, current=None):
        archivo =(x for x in self.fileManager if x.hash == file)
        self.filelist.remove(archivo)
        self.fileManager.removeFile(archivo)
    def replyNewFrontend(self, oldFrontend, current=None):
        print(oldFrontend)
        print("hola")
        #self = oldFrontend
class Frontend(Ice.Application):
    def get_topic_manager(self):
        key = 'IceStorm.TopicManager.Proxy'
        proxy = self.communicator().propertyToProxy(key)
        if proxy is None:
            print("property '{}' not set".format(key))
            return None

        print("Using IceStorm in: '%s'" % key)
        return IceStorm.TopicManagerPrx.checkedCast(proxy)
    def run(self, argv):
        broker = self.communicator()
        #frontendUpdates = FrontendUpdatesI()
        #frontendUpdates.newFrontend(self)
        
        proxy = broker.stringToProxy('filemanager1 -t -e 1.1 @ FileManagerAdapter')
        #proxy = self.communicator().stringToProxy('FileManager -t -e 1.1:tcp -h 172.25.72.183 -p 7071 -t 60000')
        fileManager = URFS.FileManagerPrx.checkedCast(proxy)
        servant = FrontendI(fileManager)
        adapter = broker.createObjectAdapter("FrontendAdapter")
        proxy = adapter.add(servant, broker.stringToIdentity("frontend1"))
        print(proxy, flush=True)

        adapter.activate()
        self.shutdownOnInterrupt()
        broker.waitForShutdown()

        return 0
frontend = Frontend()
sys.exit(frontend.main(sys.argv))
