#!/bin/bash

# Check if the script is being sourced
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  echo "Error: This script can only be executed using the 'source' command."
  echo "Please run 'source delete_customer.sh <ID>' to execute the script."
  exit 1
fi

# Load configuration variables
source ../config.conf

# Retrieve the ID from the command-line argument
ID=$1

# Check if the ID is provided
if [ -z "$ID" ]; then
  echo "Please provide an ID"
  return
fi

# Perform the deletion using cURL
echo "Deleting a Customer by ID=$ID"
response=$(curl -s -o /dev/null -w "%{http_code}" -X DELETE http://$HOSTNAME:5000/customers/$ID)
echo "========"
echo "response"
echo "========"
echo $response
echo "========"

# Check the response code
if [ "$response" -eq 200 ]; then
  echo "Customer deleted successfully"
elif [ "$response" -eq 404 ]; then
  echo "Customer not found"
else
  echo "An error occurred during the deletion (probably due to referential integrity such as can't delete customer if orders exists for that customer)"
fi