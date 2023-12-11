import sys
import Ice
import os

Ice.loadSlice('Frontend.ice')
import ServerSide
class FileUploaderI(ServerSide.FileUploader):
    def __init__(self, file_path):
        self.file_path = file_path

    def upload(self):
        print(f"Uploading {self.file_path} to the cloud")
class FileUploader:
    def __init__(self, file_path):
        self.file_path = file_path

    def upload(self):
        print(f"Uploading {self.file_path} to the cloud")