#!/usr/bin/env bash

rm -rf ./volumes/*

docker stop $(docker ps -qa) 
docker rm $(docker ps -qa) 
docker rmi -f $(docker images -qa) 
docker volume rm $(docker volume ls -q) 
docker network rm $(docker network ls -q) 
docker system prune -a -f