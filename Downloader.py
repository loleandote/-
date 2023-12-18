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
        print(data)
        data = str(binascii.b2a_base64(data, newline=False))
        print(f"Downloading {self.file} from the cloud")
        return data
    def destroy(self, current):
        current.adapter.remove(current.id)
        print(f'{self.file} destroyed', flush=True)