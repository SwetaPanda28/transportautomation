__author__ = 'vivek'

from twilio.rest import Client

account_sid = "AC367de9458730f8272b3a8b6e93584430" # Your Account SID from www.twilio.com/console
auth_token  = "f8326a61c0ded4bd610480b1dcf17845"  # Your Auth Token from www.twilio.com/console

client = Client(account_sid, auth_token)

message = client.messages.create(body="#IP#123456#24.57.144.202#8001#",
    to="+13136577876",    # Replace with your phone number
    from_="+15208605819") # Replace with your Twilio number

print(message.sid)