# This is a function called `print_coap_header` that takes a `message` object as input and prints out the CoAP header and options of the message.
# This function is useful for debugging CoAP messages, as it can provide more detailed information about the message header and options.

def print_coap_header(message):
    # Print the CoAP header
    print("CoAP Header:")
    print(f"  Version: {message.version}")  # Print the CoAP version
    print(f"  Type: {message.mtype}")  # Print the CoAP message type
    print(f"  Token Length: {len(message.token)}")  # Print the length of the CoAP token
    print(f"  Code: {message.code}")  # Print the CoAP message code
    print(f"  Message ID: {message.mid}")  # Print the CoAP message ID

    # Print the message options
    print("Options:")
    for option_number, option_value in message.opt.option_list():
        print(f"  {option_number}: {option_value}")  # Print each CoAP option number and value pair
