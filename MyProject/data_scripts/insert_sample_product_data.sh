#!/bin/bash
source ../config.conf
echo "HOSTNAME=${HOSTNAME}"
echo "Inserting a Sample Product"

# Insert a product
curl -X POST -H "Content-Type: application/json" -d @sample_product_data.json http://${HOSTNAME}:5000/products

