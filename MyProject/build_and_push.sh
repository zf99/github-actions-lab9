#!/bin/bash
REPO_NAME="<your_dockerhub_username>" #Replace with your GitHub Username
# Build, tag, and push to DockerHub
docker build -t $REPO_NAME/my_app:latest .
docker push $REPO_NAME/my_app:latest