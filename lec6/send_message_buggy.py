"""Defines a function to send a message to all recipients and yourself"""
from typing import List

def send_message_and_cc_self(message:str, sender:str, recipients:List[str]=[]) -> None:
    """Sends a message to all recipients and yourself"""
    recipients.append(sender) # add sender to recipients so they recieve a copy
    for r in recipients: #send message to each recipient
        print(f"Sending '{message}' from {sender} to {r}")

send_message_and_cc_self("note to self", "Rasika")
send_message_and_cc_self("use RSA next time", "Eve", ["Alice", "Bob"])
send_message_and_cc_self("note to self", "admin")

###line 6 changes default list (mutable), which causes error
