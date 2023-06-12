import json
import uuid
import requests
from .models import Payment
from Ticket.models import Ticket
from django.conf import settings
from Eventify.models import Event
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail
from .collectives.sendMail import SendMail
from django.shortcuts import render, redirect
from .collectives.generateCode import GenerateCode
from django.shortcuts import get_object_or_404

# Create your views here.
def payment(request, id):
    ticket = Ticket.objects.get(id=id)
    context = {'amount': ticket.price, 'event': ticket.event_id.name, 'ticket': ticket}
    return render(request, 'payment.html', context)

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
    if res['status'] == 'success':
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

    genCode = uuid.uuid4()
    code = str(genCode)
    eventName = 'New Year Event'
    amountPaid = 2700
    ticketName = 'regular'


    email = 'charlykso121@gmail.com'
    subject = 'Second one'
    message = "This is the second message"
    
    # generate QRCode
    byte_stream = GenerateCode.genQRCode(email, eventName, amountPaid, code, ticketName)

    # send mail message
    sent_count = SendMail.send_email_to_user(email, subject, message, byte_stream)
    if sent_count == 1:
        # Email was sent successfully
        messages.success(request, "Email sent successfully!")
    else:
        # Email sending failed
        messages.error(request, "Failed to send email")
    print(sent_count)
    return redirect('/')

def getCode(request):
    genCode = uuid.uuid4()
    code = str(genCode)
    email = 'charlykso121@gmail.com'
    eventName = 'New Year Event'
    amountPaid = 2700
    ticketName = 'regular'

    response = GenerateCode.genQRCode(email, eventName, amountPaid, code, ticketName)

    return response

def present(request, email, code):
    return HttpResponse('You are welcome: {} and your code is {}'.format(email, code))
