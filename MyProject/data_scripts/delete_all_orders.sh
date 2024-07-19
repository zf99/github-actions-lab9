#!/bin/bash
source ../config.conf
echo "HOSTNAME=${HOSTNAME}"
echo "Deleting all Orders"
curl -X DELETE http://localhost:5000/orders
