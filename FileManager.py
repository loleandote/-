#!/usr/bin/python3 -u

import sys
import Ice
import os
import Uploader
Ice.loadSlice('urfs.ice')
import URFS


class FileManagerI(URFS.FileManager):
    
    def __init__(self, carpeta):
        self.carpeta = carpeta
        print("Holas")
    def createUploader(self, file, current=None):
        print(f"Uploading {file} to the cloud")
class FileManager(Ice.Application):
    def run(self, argv):
        broker = self.communicator()
        servant = FileManagerI(argv)

        adapter = broker.createObjectAdapter("FileManagerAdapter")
        proxy = adapter.add(servant, broker.stringToIdentity("FileManager"))

        print(proxy, flush=True)

        adapter.activate()
        self.shutdownOnInterrupt()
        broker.waitForShutdown()

        return 0


fileManager = FileManager(sys.argv[2])
sys.exit(fileManager.main(sys.argv))
