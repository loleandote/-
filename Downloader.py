import Ice
Ice.loadSlice('ufs.ice')
import URFS

class DownloaderI(URFS.Downloader):

    def __init__(self, file):
        self.file = file
    def download(self, current=None):
        print(f"Downloading {self.file} from the cloud")
        return str.encode("hola")
    def destroy(self, current):
        current.adapter.remove(current.id)
        print(f'{self.name} destroyed', flush=True)