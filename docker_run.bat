docker rm -f uploaderr
docker image rm uploaderr:1

docker build --tag uploaderr:1 .
docker run --name uploaderr -p 8094:8094 -d uploaderr:1 

