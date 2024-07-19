#!/bin/bash
source ../config.conf
echo "HOSTNAME=${HOSTNAME}"
echo "Deleting all Products"
curl -X DELETE http://localhost:5000/products