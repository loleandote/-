#!/usr/bin/python3

import sys
import binascii

import Ice
import argparse

Ice.loadSlice('urfs.ice')
import URFS
BLOCK_SIZE = 1024

class Client(Ice.Application):
    def run(self, argv):
        ic = self.communicator()
        # properties = ic.getProperties()
        # proxy_string = properties.getProperty('Frontend.Proxy')
        # proxy = ic.stringToProxy(proxy_string)
        proxy = self.communicator().stringToProxy('Frontend -t -e 1.1:tcp -h 172.28.202.67 -p 7070 -t 60000')
        self.frontend = URFS.FrontendPrx.checkedCast(proxy)
       

        if not self.frontend:
            raise RuntimeError('Invalid proxy')

        if ARGS.list:
            self.list_request()

        if ARGS.download:
            self.download_request(ARGS.download)

        if ARGS.upload:
            self.upload_request(ARGS.upload)

        if ARGS.remove:
            self.remove_file(ARGS.remove)
            
       
        #frontend.prueba(bites)
        # downloader=frontend.downloadFile("holawkf")
        # bytes= 1024
        # resultado=[]
        # i=0
        # while i<3:
        #     resultado.append(downloader.download())
        #     bytes=len(resultado)
        #     i+=1
        # print(resultado)
        # downloader.destroy()
        # for f in ficheros:
        #     print(f)
        return 0
    
    # llama bien a la funcion listFiles del frontend
    def list_request(self):
        archivos = self.frontend.listFiles()
        for archivo in archivos:
            print(f'{archivo.name}: {archivo.hash}', flush=True)
    # No seguro
    def upload_request(self, file_name):
        try:
            uploader = self.frontend.uploadFile(file_name)
        except URFS.FileNameInUseError:
            print('File name already in use', flush=True)
            return
        with open(file_name, 'rb') as _file:
            while True:
                data = _file.read(BLOCK_SIZE)
                if not data:
                    break
                data = str(binascii.b2a_base64(data, newline=False))
                uploader.send(data)

        try:
            file_info = uploader.save()
        except URFS.FileAlreadyExistsError as e:
            print(f'File already exists: {e.hash}', flush=True)
            uploader.destroy()
            return

        uploader.destroy()
        print('Upload finished!', flush=True)
        print(f'{file_info.name}: {file_info.hash}', flush=True)
    # Todavia hay que comprobarlo
    def download_request(self, file_hash):
        try:
            downloader = self.frontend.dowloadFile(file_hash)
        except URFS.FileNameInUseError:
            print('File hash already in use', flush=True)
            return
        with open(file_hash, 'wb') as _file:
            while True:
                data =  downloader.recv(data)
                if not data:
                    break
                file_hash.write(data)
        downloader.destroy()
        print('Download finished!', flush=True)
    # No probado en ninguna versión
    def remove_file(self, file_hash):
        try:
            self.frontend.removeFile(file_hash)
        except URFS.FileNotFoundError:
            print('File not found', flush=True)
            return
        print('File removed', flush=True)
if __name__ == '__main__':
    my_parser = argparse.ArgumentParser()
    my_group = my_parser.add_mutually_exclusive_group(required=False)

    my_group.add_argument('-u', '--upload',
        help='Upload a file to the system, given its path',
        action='store',
        type=str,)
    my_group.add_argument('-d', '--download',
        help='Download a file from the system, given its hash',
        action='store',
        type=str,)
    my_group.add_argument('-r', '--remove',
        help='Remove a file from the system, given its hash',
        action='store',
        type=str,)
    my_group.add_argument('-l', '--list',
        help='List all files in the system',
        action='store_true',
        default=False)
    
    ARGS, unknown = my_parser.parse_known_args()
    sys.exit(Client().main(sys.argv))
