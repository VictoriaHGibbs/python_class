def show_messages(messages):
    """Prints a list."""
    for message in messages:
        print(f"{message}")


def send_messages(messages, sent_messages):
    """Prints a list and moves each item to a new list."""
    print("Sent messages:")
    while messages:
        in_process = messages.pop()
        print(in_process)
        sent_messages.append(in_process)


messages = ['Hey are you busy?', 'Want to grab lunch?', 'Can I call you?']

show_messages(messages)

sent_messages = []

send_messages(messages, sent_messages)

print("\nPrinting lists:")
print(messages)
print(sent_messages)
