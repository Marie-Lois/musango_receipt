import uuid

print("Musango Receipt")

print("Tell: 00237 000 800")
print("Email: info@musangobusservice.com")
print("Musango Bus Service Co. Ltd.")
user = input("User Name: ")


import datetime
Date = datetime.datetime.now()
date_now = f"Date: {Date.strftime('%Y-%m-%d')}."
print(date_now)

unique_id = uuid.uuid4()
print(f"Tracking Id: {unique_id}")
#print("Tracking Id: PARMLE1730560283")
name1 = input("Sender Name: ")
number1 = input("Sender Phone: ")
name2 = input("Receiver Name: ")
number2 = input("Receiver Number: ")
location1 = input("From: ")
location2 = input("To: ")
delivery = input("Deliver Counter: ")
payment = input("Payment Type: ")
status = input("Payment Status: ")
bus = input("Bus Number: ")

print("clothing(1 PCS) 01*1000-1000")
print("Note: small white black dotted plastic")



#print(Date.strftime("%y:%m:%d"))

