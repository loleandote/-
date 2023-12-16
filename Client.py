#!/usr/bin/python3

import sys
import Ice
Ice.loadSlice('urfs.ice')
import URFS


class Client(Ice.Application):
    def run(self, argv):
        proxy = self.communicator().stringToProxy(argv[1])
        print(argv[1])
        frontend = ServerSide.FrontendPrx.checkedCast(proxy)

        if not frontend:
            raise RuntimeError('Invalid proxy')

        #print(frontend.write('Hello World!'))
        #ficheros=frontend.list()
        bites= str.encode("hola")
        #frontend.prueba(bites)
        downloader=frontend.downloadFile("holawkf")
        bytes= 1024
        resultado=[]
        i=0
        while i<3:
            resultado.append(downloader.download())
            bytes=len(resultado)
            i+=1
        print(resultado)
        downloader.destroy()
        # for f in ficheros:
        #     print(f)
        return 0


sys.exit(Client().main(sys.argv))
