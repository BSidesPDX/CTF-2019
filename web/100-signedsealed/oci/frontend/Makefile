OCIR_URL := phx.ocir.io
TENANCY := oke
REGISTRY := bsidespdx2019
DOCKER_IMAGE := web100_frontend

CONTAINER_TAG := ${OCIR_URL}/${TENANCY}/${REGISTRY}/${DOCKER_IMAGE}

target: container push deploy serve

clean: deleteDocker deleteKube

# Docker Configurations

container:
	docker build --build-arg API_URL=http://$(shell ./get_backend_ip.sh):48323 --no-cache --tag ${CONTAINER_TAG} ../../src/frontend/

push: 
	docker push ${CONTAINER_TAG}

deleteDocker:
	docker image rm ${CONTAINER_TAG}

# Kubernetes

deploy:
	cat deployment/deploy.yaml | kubectl create --namespace bsidespdxctf  -f -

serve:
	kubectl create --namespace bsidespdxctf -f deployment/service.yaml

deleteKube:
	cat deployment/deploy.yaml | kubectl delete --namespace bsidespdxctf -f -
	kubectl delete --namespace  bsidespdxctf -f deployment/service.yaml
