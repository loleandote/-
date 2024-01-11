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

run-fileManager:
	mkdir -p storage
	python3 ./FileManager.py --Ice.Config=filemanager1.config 

run-frontend:
	python3 ./Frontend.py --Ice.Config=frontend1.config $(NUM_FILEMANAGERS)

test-client:
	mkdir -p downloads
	python3 ./Client.py --Ice.Config=client.config --upload $(FILE)
	python3 ./Client.py --Ice.Config=client.config --list
	python3 ./Client.py --Ice.Config=client.config --download $(FILE_HASH)
#	./Client.py --Ice.Config=client.config --remove $(FILE_HASH)
#	./Client.py --Ice.Config=client.config --list

run-icestorm:
	mkdir -p IceStorm/
	icebox --Ice.Config=icebox.config

run-registry:
	mkdir -p data/db/registry
	icegridregistry --Ice.Config=registry.config

clean:
	$(RM) -r downloads/ storage/ __pycache__/ URFS/
	$(RM) urfs_ice.py *.pyc
vclean: clean
	$(RM) -r IceStorm/ data/

