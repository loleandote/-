import Ice

Ice.loadSlice('urfs.ice')
import URFS
class UploaderI(URFS.Uploader):
    def __init__(self, file):
        self.file = file
        print(file)

    def send(self, data):
        print(f"Uploading {self.file} to the cloud")
    
    def destroy(self, current):
        print(f"Destroying {self.file}")
        current.adapter.remove(current.id)