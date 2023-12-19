#!/usr/bin/python3 -u

import sys
from Downloader import DownloaderI
from Uploader import UploaderI
import Ice
import os
import Uploader
Ice.loadSlice('urfs.ice')
import URFS


class FileManagerI(URFS.FileManager):
    
    # def __init__(self, carpeta):
    #     self.carpeta = carpeta
    def createUploader(self, filename, current):
        servant = UploaderI(filename)
        proxy = current.adapter.addWithUUID(servant)
        return URFS.UploaderPrx.checkedCast(proxy)
    def createDownloader(self, hash, current):
        servant = DownloaderI(hash)
        proxy = current.adapter.addWithUUID(servant)
        return URFS.DownloaderPrx.checkedCast(proxy)
    def removeFile(self, hash, current=None):
        os.remove('storage/'+hash)
        print(f"Removing {hash} from the cloud")
class FileManager(Ice.Application):
    def run(self, argv):
        broker = self.communicator()
        servant = FileManagerI()
        adapter = broker.createObjectAdapter("FileManagerAdapter")
        proxy = adapter.add(servant, broker.stringToIdentity("filemanager1"))

        print(proxy, flush=True)

        adapter.activate()
        self.shutdownOnInterrupt()
        broker.waitForShutdown()

        return 0


fileManager = FileManager()
sys.exit(fileManager.main(sys.argv))
