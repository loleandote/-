import Ice
Ice.loadSlice('urfs.ice')
import URFS
import binascii

class DownloaderI(URFS.Downloader):

    def __init__(self, file):
        self.file = file
        archivo ='storage/'+self.file
        self.fichero=open(archivo, 'rb')
    def recv(self,size, current=None):
        data=None
        data = self.fichero.read(size)
        data = str(binascii.b2a_base64(data, newline=False))
        return data
    def destroy(self, current):
        print(f"Destroying {current.id}")
        current.adapter.remove(current.id)