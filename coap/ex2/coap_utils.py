def print_coap_header(message):
    print("CoAP Header:")
    print(f"  Version: {message.version}")
    print(f"  Type: {message.mtype}")  # Change 'type' to 'mtype'
    print(f"  Token Length: {len(message.token)}")
    print(f"  Code: {message.code}")
    print(f"  Message ID: {message.mid}")

    print("Options:")
    for option_number, option_value in message.opt.option_list():
        print(f"  {option_number}: {option_value}")
