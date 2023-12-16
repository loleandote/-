import sys
import Ice
import os

Ice.loadSlice('urfs.ice')
import URFS
class UploaderI(URFS.Uploader):
    def __init__(self, file_path):
        self.file_path = file_path

    def send(self):
        print(f"Uploading {self.file_path} to the cloud")
class Uploader:
    def __init__(self, file_path):
        self.file_path = file_path

    def send(self):
        print(f"Uploading {self.file_path} to the cloud")