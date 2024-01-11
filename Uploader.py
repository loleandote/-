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
        data = data[1:]
        data= binascii.a2b_base64(data)
        self.fichero.write(data)

    def save(self, current=None):
        print(f"Saving {self.file} to the cloud")
        return URFS.FileInfo(self.file, hashlib.md5(open(self.file,'rb').read()).hexdigest())

    def destroy(self, current):
        print(f"Destroying {current.id}")
        current.adapter.remove(current.id)