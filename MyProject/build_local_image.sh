#!/bin/bash
REPO_NAME="<your_dockerhub_username>" #Replace with your GitHub Username
docker build -t $REPO_NAME/my_app:latest .