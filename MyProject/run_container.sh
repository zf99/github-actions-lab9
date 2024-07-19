#!/bin/bash
REPO_NAME="<your_dockerhub_username>" #Replace with your GitHub Username
docker stop my_app
docker rm my_app
docker pull $REPO_NAME/my_app:latest
docker run -p 5001:5000 --name my_app $REPO_NAME/my_app:latest