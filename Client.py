#!/usr/bin/python3

import sys
import Ice
Ice.loadSlice('urfs.ice')
import URFS


class Client(Ice.Application):
    def run(self, argv):
        proxy = self.communicator().stringToProxy(argv[1])
        print(argv[1])
        printer = URFS.FrontendPrx.checkedCast(proxy)

        if not printer:
            raise RuntimeError('Invalid proxy')

        #print(printer.write('Hello World!'))
        #ficheros=printer.list()
        bites= str.encode("hola")
        printer.prueba(bites)
        # for f in ficheros:
        #     print(f)
        return 0


sys.exit(Client().main(sys.argv))
