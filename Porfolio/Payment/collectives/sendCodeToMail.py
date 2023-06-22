from .generateCode import GenerateCode
from .sendMail import SendMail

def sendCodeToMail(email, eventName, amountPaid, code, ticketName, quantity):

    subject = f'Your ticket for {eventName} event'
    message = f"Your payment was successfuly recieved. \nAmount paid: \u20a6{amountPaid} for the event: {eventName}. \nBelow is your ticket"

    # generate QRCode
    byte_stream = GenerateCode.genQRCode(
        email, eventName, amountPaid, code, ticketName, quantity)

    # send mail message
    sent_count = SendMail.send_email_to_user(
        email, subject, message, byte_stream)
    
    print(sent_count)
    return sent_count