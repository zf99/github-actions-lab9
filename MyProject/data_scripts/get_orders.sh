#!/bin/bash
source ../config.conf
echo "HOSTNAME=${HOSTNAME}"
echo "Getting all Orders"
# Get Orders
curl http://${HOSTNAME}:5000/orders