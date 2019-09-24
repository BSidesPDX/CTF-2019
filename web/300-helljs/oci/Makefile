OCIR_URL := phx.ocir.io
TENANCY := oke
REGISTRY := bsidespdx2019
DOCKER_IMAGE := web300

CONTAINER_TAG := ${OCIR_URL}/${TENANCY}/${REGISTRY}/${DOCKER_IMAGE}

target: container push deploy serve

clean: deleteDocker deleteKube

# Docker Configurations

container:
	docker build --no-cache --tag ${CONTAINER_TAG}_vulnerable_backend ../src/vulnerable-backend/
	docker build --no-cache --tag ${CONTAINER_TAG}_secure_backend ../src/secure-backend/
	docker build \
	--build-arg VULNERABLE_API_URL=http://web300backend-a.bsidespdxctf.party:27331 \
	--build-arg SECURE_API_URL=http://web300backend-b.bsidespdxctf.party:27332 \
	--no-cache --tag ${CONTAINER_TAG}_frontend ../src/frontend/

push:
	docker push ${CONTAINER_TAG}_vulnerable_backend
	docker push ${CONTAINER_TAG}_secure_backend
	docker push ${CONTAINER_TAG}_frontend

deleteDocker:
	docker image rm ${CONTAINER_TAG}_vulnerable_backend
	docker image rm ${CONTAINER_TAG}_secure_backend
	docker image rm ${CONTAINER_TAG}_frontend

# Kubernetes

deploy:
	cat deployment/deploy_vulnerable_backend.yaml | kubectl create --namespace bsidespdxctf  -f -
	cat deployment/deploy_secure_backend.yaml | kubectl create --namespace bsidespdxctf  -f -
	cat deployment/deploy_frontend.yaml | kubectl create --namespace bsidespdxctf  -f -

serve:
	kubectl create --namespace bsidespdxctf -f deployment/service_vulnerable_backend.yaml
	kubectl create --namespace bsidespdxctf -f deployment/service_secure_backend.yaml
	kubectl create --namespace bsidespdxctf -f deployment/service_frontend.yaml

deleteKube:
	cat deployment/deploy_vulnerable_backend.yaml | kubectl delete --namespace bsidespdxctf -f -
	cat deployment/deploy_secure_backend.yaml | kubectl delete --namespace bsidespdxctf -f -
	cat deployment/deploy_frontend.yaml | kubectl delete --namespace bsidespdxctf -f -
	kubectl delete --namespace  bsidespdxctf -f deployment/service_vulnerable_backend.yaml
	kubectl delete --namespace  bsidespdxctf -f deployment/service_secure_backend.yaml
	kubectl delete --namespace  bsidespdxctf -f deployment/service_frontend.yaml
