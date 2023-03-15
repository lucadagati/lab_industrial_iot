#!/bin/bash

# Get the current state of the bulb
echo "Getting the current state of the bulb:"
curl -X GET http://localhost:5000/bulb
echo
echo

# Turn the bulb on
echo "Turning the bulb on:"
curl -X PUT -H "Content-Type: application/json" -d '{"status": "on"}' http://localhost:5000/bulb
echo
echo

# Turn the bulb off
echo "Turning the bulb off:"
curl -X PUT -H "Content-Type: application/json" -d '{"status": "off"}' http://localhost:5000/bulb
echo
echo

# Set the bulb brightness to 50%
echo "Setting the bulb brightness to 50%:"
curl -X PUT -H "Content-Type: application/json" -d '{"brightness": 50}' http://localhost:5000/bulb
echo
