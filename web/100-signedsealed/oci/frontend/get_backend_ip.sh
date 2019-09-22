#!/usr/bin/env bash
kubectl get services web100-backend --namespace bsidespdxctf | grep LoadBalancer | awk '{print $4}'
