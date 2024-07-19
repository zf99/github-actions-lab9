#!/bin/bash
# Load configuration variables
source ../config.conf
echo "HOSTNAME=${HOSTNAME}"
# Perform the deletion using cURL
echo "Deleting a Customer by ID=1"
curl -X DELETE http://${LOCALHOST}:5000/customers/1