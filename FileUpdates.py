import Ice
Ice.loadSlice('urfs.ice')
import URFS
class FIleUpdatesI(URFS.FIleUpdates):
    def new(self, file, current=None):
        pass
    def removed(self, file, current=None):
        pass