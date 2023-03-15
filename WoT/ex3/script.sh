#!/bin/bash

function get_device_state() {
    local device_name=$1
    echo "Getting the state of the $device_name:"
    curl -X GET http://localhost:5000/devices/$device_name
    echo
    echo
}

function update_device_state() {
    local device_name=$1
    local new_state=$2
    echo "Updating the state of the $device_name:"
    curl -X PUT -H "Content-Type: application/json" -d "$new_state" http://localhost:5000/devices/$device_name
    echo
    echo
}

# Get the current state of all devices
get_device_state "bulb"
get_device_state "thermostat"
get_device_state "door_lock"

# Turn the bulb on
update_device_state "bulb" '{"status": "on"}'

# Set the thermostat to heating mode and temperature to 24 degrees
update_device_state "thermostat" '{"mode": "heat", "temperature": 24}'

# Unlock the door
update_device_state "door_lock" '{"status": "unlocked"}'
