#!/bin/bash
docker stop my_app
docker rm my_app
docker run -p 5001:5000 --name my_app my_app:latest