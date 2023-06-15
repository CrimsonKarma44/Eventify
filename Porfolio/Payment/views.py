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
from .collectives.makePayment import initiate_payment


# Create your views here.
def payment(request, id):
    ticket = Ticket.objects.get(id=id)
    tx_ref = uuid.uuid4().hex[:10]
    context = {'amount': ticket.price, 'event': ticket.event_id.name, 'ticket': ticket, 'ticket_id': id, 'tx_ref': tx_ref}
    return render(request, 'payment.html', context)

def make_payment(request, id):
    # Collect the necessary payment details from the request
    event = Event.objects.get(id=id)
    email = request.POST.get('email')
    phone_number = request.POST.get('phoneNo')
    quantity = request.POST.get('quantity')
    amount = request.POST.get('amount')
    totalAmount = (float(amount) * int(quantity)) * 100
    tx_ref = request.POST.get('tx_ref')
    ticket_id = request.POST.get('ticket_id')
    redirect_url = request.POST.get('redirect_url')
    userData = {
        'email': email,
        'amount': totalAmount,
        'reference': tx_ref,
        'callback_url': redirect_url,
        'metadata': json.dumps({'quantity': quantity, 'phone_number': phone_number, 'ticket_id': ticket_id})
    }
    headers = {
        "Authorization": "Bearer sk_test_c7c794bf42d409179d35cf75f239a5949790ee49",
        "Content-Type": "application/json"
    }
    

    try:
        response = requests.post('https://api.paystack.co/transaction/initialize', headers=headers, json=userData)
        if response.status_code == 200:
            # Request successful
            json_response = response.json()
            # print(json_response)
            # Extract the access code from the response
            authorization_url = json_response['data']['authorization_url']

            # Redirect the user to the Paystack payment page
            return redirect(authorization_url)
        else:
            # Request failed
            error_message = response.text
            # Handle the error as needed
            return HttpResponseServerError(error_message)
    except Exception as e:
        print(f"The exception: {e}")
        return HttpResponse(f"The exception: {e}")
    return HttpResponse(res)


def payment_callback(request):
    # Process the payment callback
    response = request.GET
    reference = response['reference']
    # print(reference)
    headers = {
        "Authorization": "Bearer sk_test_c7c794bf42d409179d35cf75f239a5949790ee49"
    }
    res = requests.get('https://api.paystack.co/transaction/verify/{}'.format(reference), headers=headers)
    res = res.json()

    print(res)
    
    # # You can verify the payment status and update your database accordingly
    if res['status'] == 'success':
        ticket_id = res['data']['ticket_id']
        amount = res['data']['amount']
        email = res['data']['authorization']['customer']['email']
        phone_no = res['data']['metadata']['phone_number']
        quantity = res['data']['metadata']['quantity']
        status = res['data']['status']
        genCode = uuid.uuid4()
        code = str(genCode)
    #     payment = Payment(ticket_id=ticket_id, price=amount, email=email, code=code, phone_no=phone_no)
    #     payment.save()
    #     ticket = Ticket.object.get(id=ticket_id)
    #     if ticket is not None:
    #         event = ticket.event_id.name
    #         qrcode = GenerateCode.genQRCode(email, event, amount, code, ticket_id)
    #     messages.success(request, "Payment made successfully!")
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
