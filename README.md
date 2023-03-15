# IoT Communication Protocols: CoAP, MQTT, WAMP, and WoT

This repository covers the fundamentals of four popular Internet of Things (IoT) communication protocols: Constrained Application Protocol (CoAP), Message Queuing Telemetry Transport (MQTT), Web Application Messaging Protocol (WAMP), and Web of Things (WoT).

## CoAP

CoAP is a web transfer protocol designed for resource-constrained devices and networks. It follows the REST architecture, making it suitable for IoT devices with limited processing power, memory, and bandwidth. CoAP uses the User Datagram Protocol (UDP) for communication.

### Features:

- Lightweight
- Asynchronous message exchange
- Support for the observe pattern
- Built-in discovery mechanism

## MQTT

MQTT is a lightweight messaging protocol for small sensors and mobile devices. It follows the publish-subscribe pattern and is optimized for high-latency or unreliable networks. MQTT uses the Transmission Control Protocol (TCP) for communication.

### Features:

- Publish-subscribe model
- Lightweight
- QoS levels for message delivery
- Last Will and Testament (LWT) support

## WAMP

WAMP is a protocol that combines the features of Remote Procedure Calls (RPC) and Publish-Subscribe (PubSub) messaging patterns. It is designed for real-time distributed systems and uses WebSockets for communication.

### Features:

- Remote Procedure Calls (RPC)
- Publish-Subscribe (PubSub) messaging
- Real-time communication
- WebSocket transport

## WoT

WoT (Web of Things) is not a protocol but a concept that aims to apply web standards and technologies to IoT devices. It provides a framework for integrating IoT devices into the World Wide Web by exposing their data and functionalities through web APIs.

### Features:

- Web APIs for IoT devices
- Seamless integration of IoT devices into the web
- Semantic descriptions for better interoperability
- Standardization and security
