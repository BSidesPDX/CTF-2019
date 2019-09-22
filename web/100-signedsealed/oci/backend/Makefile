OCIR_URL := phx.ocir.io
TENANCY := oke
REGISTRY := bsidespdx2019
DOCKER_IMAGE := web100_backend

CONTAINER_TAG := ${OCIR_URL}/${TENANCY}/${REGISTRY}/${DOCKER_IMAGE}

target: container push deploy serve

clean: deleteDocker deleteKube

# Docker Configurations

container:
	docker build --no-cache --tag ${CONTAINER_TAG} ../../src/backend/

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
