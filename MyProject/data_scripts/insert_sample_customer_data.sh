#!/bin/bash
source ../config.conf
echo "HOSTNAME=${HOSTNAME}"
echo "Inserting a sample Customer"
# Insert a customer
curl -X POST -H "Content-Type: application/json" -d @sample_customer_data.json http://${HOSTNAME}:5000/customers