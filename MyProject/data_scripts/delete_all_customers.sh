#!/bin/bash
source ../config.conf
echo "HOSTNAME=${HOSTNAME}"
echo "Deleting all Customers"
curl -X DELETE http://localhost:5000/customers
