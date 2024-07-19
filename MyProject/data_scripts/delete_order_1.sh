#!/bin/bash
# Load configuration variables
source ../config.conf
echo "HOSTNAME=${HOSTNAME}"
# Perform the deletion using cURL
echo "Deleting a Order by ID=1"
curl -X DELETE http://${HOSTNAME}:5000/orders/1