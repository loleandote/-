#!/usr/bin/make -f
#A la hora de entregar eliminar el comando python3
NUM_FILEMANAGERS ?= 1
FILE ?= example.png
FILE_HASH ?= $(shell md5sum $(FILE) | cut -d' ' -f1)


start:
	$(MAKE) run-icestorm & $(MAKE) run-registry &
	sleep 1
	$(MAKE) run-filemanager &
	sleep 1
	$(MAKE) run-frontend
clean:
	$(RM) -r *~ proxy.out Printer_ice.py Example/

run-frontend:
	python3 ./Frontend.py --Ice.Config=frontend1.config $(NUM_FILEMANAGERS)
#./Server.py --Ice.Config=Server.config | tee proxy.out

run-fileManager:
	mkdir -p storage
	python3 ./FileManager.py --Ice.Config=filemanager1.config 

run-client:
	python3 ./Client.py '$(shell head -1 proxy.out)'
test-client:
	mkdir -p downloads
	python3 ./Client.py --Ice.Config=client.config --upload $(FILE)
#python3 ./Client.py --Ice.Config=client.config --list
#./Client.py --Ice.Config=client.config --download $(FILE_HASH)
#./Client.py --Ice.Config=client.config --remove $(FILE_HASH)
#./Client.py --Ice.Config=client.config --list
#./Client.py '$(shell head -1 proxy.out)'

gen-src:
	slice2py Frontend.ice
