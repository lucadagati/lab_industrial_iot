#!/bin/bash

echo "Getting weather data from the weather station:"
curl -X GET http://localhost:5000/weather
echo
