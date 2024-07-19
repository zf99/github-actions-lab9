#!/bin/bash
source ../config.conf
echo "HOSTNAME=${HOSTNAME}"
echo "Getting all Customers"
# Get Customers
curl http://${HOSTNAME}:5000/customers