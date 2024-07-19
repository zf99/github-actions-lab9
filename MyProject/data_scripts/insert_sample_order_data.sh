#!/bin/bash
#!/bin/bash
source ../config.conf
echo "HOSTNAME=${HOSTNAME}"
echo "Inserting a sample Order"

# Insert an order
curl -X POST -H "Content-Type: application/json" -d @sample_order_data.json http://${HOSTNAME}:5000/orders
