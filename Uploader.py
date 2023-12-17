import Ice

Ice.loadSlice('urfs.ice')
import URFS
class UploaderI(URFS.Uploader):
    def __init__(self, filename):
        self.filfilenamee_path = filename

    def send(self):
        print(f"Uploading {self.filename} to the cloud")
class Uploader:
    def __init__(self, file_path):
        self.file_path = file_path

    def send(self, data):
        print(f"Uploading {self.file_path} to the cloud")