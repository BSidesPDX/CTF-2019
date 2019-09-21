# bsidespdx2019 is the organization on dockerhub
OCIR_URL := phx.ocir.io
TENANCY := oke
REGISTRY := bsidespdx2019
DOCKER_IMAGE := web100

CONTAINER_TAG := ${OCIR_URL}/${TENANCY}/${REGISTRY}/${DOCKER_IMAGE}

target: container push deploy serve

clean: deleteDocker deleteKube
	make -C ../src clean

# Docker Configurations

container:
	docker build --no-cache --tag ${CONTAINER_TAG}_backend ../src/backend/
	docker build --build-arg API_URL=http://129.146.155.52:48323 --no-cache --tag ${CONTAINER_TAG}_frontend ../src/frontend/ 

push: 
	docker push ${CONTAINER_TAG}_backend
	docker push ${CONTAINER_TAG}_frontend

deleteDocker:
	docker image rm ${CONTAINER_TAG}_backend
	docker image rm ${CONTAINER_TAG}_frontend

# Kubernetes

deploy:
	cat deployment/deploy_backend.yaml | kubectl create --namespace bsidespdxctf  -f -
	cat deployment/deploy_frontend.yaml | kubectl create --namespace bsidespdxctf  -f -

serve:
	kubectl create --namespace bsidespdxctf -f deployment/service_backend.yaml
	kubectl create --namespace bsidespdxctf -f deployment/service_frontend.yaml

deleteKube:
	cat deployment/deploy_backend.yaml | kubectl delete --namespace bsidespdxctf -f -
	cat deployment/deploy_frontend.yaml | kubectl delete --namespace bsidespdxctf -f -
	kubectl delete --namespace  bsidespdxctf -f deployment/service_backend.yaml
	kubectl delete --namespace  bsidespdxctf -f deployment/service_frontend.yaml
