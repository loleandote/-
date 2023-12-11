#!/usr/bin/make -f
# -*- mode:makefile -*-

clean:
	$(RM) -r *~ proxy.out Printer_ice.py Example/

run-frontend:
	python3 ./Frontend.py --Ice.Config=Frontend.config
#./Server.py --Ice.Config=Server.config | tee proxy.out

run-fileManager:
	python3 ./FileManager.py --Ice.Config=FileManager.config ./Servidor1

run-client:
	python3 ./Client.py '$(shell head -1 proxy.out)'
#./Client.py '$(shell head -1 proxy.out)'

gen-src:
	slice2py Frontend.ice
