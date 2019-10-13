target: container push deploy serve

clean: deleteDocker deleteKube

# Docker Configurations

container:
	make -C ../pwn/100-rot13/oci/ container
	make -C ../pwn/300-pwnchess/oci/ container
	make -C ../web/100-signedsealed/oci/ container
	make -C ../web/200-yourstruly/oci/ container
	make -C ../web/300-helljs/oci/ container

push:
	make -C ../pwn/100-rot13/oci/ push
	make -C ../pwn/300-pwnchess/oci/ push
	make -C ../web/100-signedsealed/oci/ push
	make -C ../web/200-yourstruly/oci/ push
	make -C ../web/300-helljs/oci/ push

deleteDocker:
	make -C ../pwn/100-rot13/oci/ deleteDocker
	make -C ../pwn/300-pwnchess/oci/ deleteDocker
	make -C ../web/100-signedsealed/oci/ deleteDocker
	make -C ../web/200-yourstruly/oci/ deleteDocker
	make -C ../web/300-helljs/oci/ deleteDocker

# Kubernetes

deploy:
	make -C ../pwn/100-rot13/oci/ deploy
	make -C ../pwn/300-pwnchess/oci/ deploy
	make -C ../web/100-signedsealed/oci/ deploy
	make -C ../web/200-yourstruly/oci/ deploy
	make -C ../web/300-helljs/oci/ deploy

serve:
	make -C ../pwn/100-rot13/oci/ serve
	make -C ../pwn/300-pwnchess/oci/ serve
	make -C ../web/100-signedsealed/oci/ serve
	make -C ../web/200-yourstruly/oci/ serve
	make -C ../web/300-helljs/oci/ serve

deleteKube:
	make -C ../pwn/100-rot13/oci/ deleteKube
	make -C ../pwn/300-pwnchess/oci/ deleteKube
	make -C ../web/100-signedsealed/oci/ deleteKube
	make -C ../web/200-yourstruly/oci/ deleteKube
	make -C ../web/300-helljs/oci/ deleteKube
