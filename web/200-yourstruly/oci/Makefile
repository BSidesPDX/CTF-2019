OCIR_URL := phx.ocir.io
TENANCY := oke
REGISTRY := bsidespdx2019
DOCKER_IMAGE := web200

CONTAINER_TAG := ${OCIR_URL}/${TENANCY}/${REGISTRY}/${DOCKER_IMAGE}

target: container push deploy serve

clean: deleteDocker deleteKube

# Docker Configurations

container:
	docker build --no-cache --tag ${CONTAINER_TAG}_minio ../src/minio/
	docker build --no-cache --tag ${CONTAINER_TAG}_store ../src/store/
	docker build --no-cache --tag ${CONTAINER_TAG}_backend ../src/backend/

push:
	docker push ${CONTAINER_TAG}_minio
	docker push ${CONTAINER_TAG}_store
	docker push ${CONTAINER_TAG}_backend 

deleteDocker:
	docker image rm ${CONTAINER_TAG}_minio
	docker image rm ${CONTAINER_TAG}_store
	docker image rm ${CONTAINER_TAG}_backend

# Kubernetes

deploy:
	cat deployment/deploy_minio.yaml | kubectl create --namespace bsidespdxctf  -f -
	cat deployment/deploy_store.yaml | kubectl create --namespace bsidespdxctf  -f -
	cat deployment/deploy_backend.yaml | kubectl create --namespace bsidespdxctf  -f -

serve:
	kubectl create --namespace bsidespdxctf -f deployment/service_minio.yaml
	kubectl create --namespace bsidespdxctf -f deployment/service_store.yaml
	kubectl create --namespace bsidespdxctf -f deployment/service_backend.yaml

deleteKube:
	cat deployment/deploy_minio.yaml | kubectl delete --namespace bsidespdxctf -f -
	cat deployment/deploy_store.yaml | kubectl delete --namespace bsidespdxctf -f -
	cat deployment/deploy_backend.yaml | kubectl delete --namespace bsidespdxctf -f -
	kubectl delete --namespace  bsidespdxctf -f deployment/service_minio.yaml
	kubectl delete --namespace  bsidespdxctf -f deployment/service_store.yaml
	kubectl delete --namespace  bsidespdxctf -f deployment/service_backend.yaml
