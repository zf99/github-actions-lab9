#!/bin/bash
source ../config.conf
echo "HOSTNAME=${HOSTNAME}"
echo "Getting all Products"
# Get Products
curl http://${HOSTNAME}:5000/products