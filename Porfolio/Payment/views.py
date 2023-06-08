from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse
from django.contrib import messages
import json
from .models import Payment
import uuid
from Ticket.models import Ticket
from Eventify.models import Event
from .collectives.generateCode import GenerateCode
from .collectives.sendMail import SendMail

# Create your views here.
def payment(request):
    return render(request, 'payment.html')

def make_payment(request):
    # Collect the necessary payment details from the request
    pass


def payment_callback(request):
    # Process the payment callback
    response = request.GET.get('response')
    response = json.loads(response)
   
    payment_id = response['id']
    headers = {
        "Authorization": "Bearer FLWSECK_TEST-6f6ed5664336aaf1ae5ee6c28f5446d9-X",
        "Content-Type": "application/json"
    }
    res = requests.get('https://api.flutterwave.com/v3/transactions/{}/verify'.format(payment_id), headers=headers)
    
    res = res.json()
    # You can verify the payment status and update your database accordingly
    if res['status'] is 'success':
        genCode = uuid.uuid4()
        code = str(genCode)
        payment = Payment(ticket_id=res['ticket_id'], prince=res['amount'], email=res['email'], code=code, phone_no=res['phoneNo'])
        payment.save()
        ticket = Ticket.object.get(id=res['ticket_id'])
        if ticket is not None:
            event = Event.object.get(id=ticket.event_id)
            if event is not None:
                qrcode = GenerateCode.genQRCode(res[email], event.name, res[amount], code, res['ticket_id'])
        messages.success(request, "Payment made successfully!")
    return redirect('/')

def send_email(request):
    email = 'charlykso141@gmail.com'
    subject = 'This is just testing'
    message = "This is the real message"
    sendIt = SendMail.send_email_to_user(email, subject, message)
    print(sendIt)