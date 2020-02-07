# we import the Twilio client from the dependency we just installed
from twilio.rest import Client

# the following line needs your Twilio Account SID and Auth Token
client = Client("AC99e9e01f137d4f28043bba819a9c8cc3", "3ccbf1dbb4fcadbf8d2923957d33f824")

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
client.messages.create(to="+19732644152", 
                       from_="+12023351278", 
                       body="Hi this is HARSH RAJORIA AND I want to say enjoy it")