CoAP Temperature Monitoring System

This project demonstrates a simple temperature monitoring system using the Constrained Application Protocol (CoAP). It consists of two main components: a server that simulates a temperature sensor and a client that can observe and receive real-time temperature updates.

Project Structure

coap_temperature_server.py: Implements a CoAP server with an observable /temperature resource. This resource simulates temperature changes over time.
coap_temperature_client.py: A CoAP client that sends a GET request to observe the /temperature resource on the server, receiving real-time temperature updates.
TemperatureResource Class

The TemperatureResource class is at the heart of the CoAP server. It extends aiocoap.resource.ObservableResource to simulate a temperature sensor. The temperature is initially set to 20°C and is updated every 5 seconds by a random amount between -0.5°C and 0.5°C. Observers of this resource are notified of these updates, allowing clients to track temperature changes in real-time.

Server Behavior

Upon receiving a standard GET request for the /temperature resource, the server responds with the current temperature value. When a client sends a GET request with the "Observe" option, it subscribes to receive updates whenever the temperature changes.

Client Behavior

The client first sends a standard GET request to retrieve and display the initial temperature. It then sends another GET request with the "Observe" option to start receiving real-time updates. These updates are printed to the console as they arrive.

Running the Example

Start the Server: Run coap_temperature_server.py to start the CoAP server. The server will begin listening for incoming requests and periodically updating the simulated temperature.

Run the Client: With the server running, execute coap_temperature_client.py to start the CoAP client. The client will display the initial temperature and print updates as they occur.

This system demonstrates the use of CoAP for real-time data monitoring in IoT applications, making it an excellent example for learning and experimentation with CoAP and observable resources.

Requirements

Python 3.7 or newer.
aiocoap library.
