#!/usr/bin/python3 -u

import sys
import Ice
import os
from FileDownloader import FileDownloaderI
import FileUploader
Ice.loadSlice('Frontend.ice')
import ServerSide


class FileManagerI(URFS.FileManager):
    
    def __init__(self, carpeta):
        self.carpeta = carpeta
        print("Holas")
    def createUploader(self, file, current=None):
        print(f"Uploading {file} to the cloud")
        return "hola"
    def createDownloader(self, file, current):
        servant = FileDownloaderI(file)
        proxy = current.adapter.addWithUUID(servant)
        return ServerSide.FileDownloaderPrx.checkedCast(proxy)
        
class FileManager(Ice.Application):
    def run(self, argv):
        broker = self.communicator()
        servant = FileManagerI(argv[1])
        adapter = broker.createObjectAdapter("FileManagerAdapter")
        proxy = adapter.add(servant, broker.stringToIdentity("FileManager"))

        print(proxy, flush=True)

        adapter.activate()
        self.shutdownOnInterrupt()
        broker.waitForShutdown()

        return 0


fileManager = FileManager()
sys.exit(fileManager.main(sys.argv))
