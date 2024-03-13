# CoAP Demo with aiocoap in Python

This repository contains a simple demonstration of a CoAP (Constrained Application Protocol) client and server using the `aiocoap` library in Python. The demo showcases how to set up a basic CoAP server that responds with "Hello, CoAP!" to GET requests, and a CoAP client that sends these requests.

## Requirements

- Python 3.7+
- aiocoap

## Installation

First, ensure you have Python 3.7 or higher installed. You can then install the `aiocoap` library using pip:

```bash
pip install aiocoap
```

## CoAP Server
The CoAP server is designed to listen for incoming CoAP GET requests on coap://127.0.0.1:5683/hello and respond with a payload containing "Hello, CoAP!".

To start the server, run:

```bash
python coap_server.py
```

The server will start and listen on 127.0.0.1:5683. It prints the CoAP header of incoming requests for debugging purposes.

## CoAP Client
The CoAP client sends a GET request to coap://127.0.0.1:5683/hello and prints the response payload.

To run the client, execute:

```bash
python coap_client.py
```
Upon successful execution, the client will display the server's response, demonstrating the interaction between the CoAP client and server.

## Utility Function
Included in this demo is a utility function print_coap_header, used by both the client and server for printing CoAP message headers for debugging and educational purposes.

