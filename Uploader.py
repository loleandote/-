import Ice

Ice.loadSlice('urfs.ice')
import URFS
import binascii
import hashlib
class UploaderI(URFS.Uploader):
    def __init__(self, file):
        self.file = file
        self.fichero=open('storage/'+self.file, 'wb')

    def send(self, data, current=None):
        archivo ='storage/'+self.file
        data = data[1:]
        data= binascii.a2b_base64(data)
        self.fichero.write(data)
        print(f"Uploading {self.file} to the cloud")
    
    def save(self, current=None):
        print(f"Saving {self.file} to the cloud")
        return URFS.FileInfo(self.file, hashlib.md5(self.fichero))

    def destroy(self, current):
        print(f"Destroying {self.file}")
        current.adapter.remove(current.id)