import json
import uuid
import requests
from .models import Payment
from Ticket.models import Ticket
from django.conf import settings
from Eventify.models import Event
from django.contrib.auth.models import User
from Eventify.models import UserProfile
from .models import Payment
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .collectives.sendCodeToMail import sendCodeToMail
# from django.core.mail import send_mail
# from .collectives.sendMail import SendMail


# Create your views here.
def payment(request, id):
    title = 'Make payment'
    ticket = Ticket.objects.get(id=id)
    tx_ref = uuid.uuid4().hex[:10]
    context = {'amount': ticket.price, 'event': ticket.event_id.name,
               'ticket': ticket, 'ticket_id': id, 'tx_ref': tx_ref, 'title': title}
    return render(request, 'payment.html', context)


def make_payment(request, id):
    # Collect the necessary payment details from the request
    event = Event.objects.get(id=id)
    owner = User.objects.get(id=event.user.id)
    user_profile = UserProfile.objects.get(user=owner)
    # print(user_profile.secret_key)
    email = request.POST.get('email')
    phone_number = request.POST.get('phoneNo')
    quantity = request.POST.get('quantity')
    amount = request.POST.get('amount')
    if int(quantity) <= 0:
        messages.error(request, "Amount not supported!")
        return redirect('/')
    totalAmount = int(float(amount) * int(quantity) * 100)
    # totalAmount = str(totalAmount)+".00"
    tx_ref = request.POST.get('tx_ref')
    ticket_id = request.POST.get('ticket_id')
    redirect_url = "http://192.168.5.148:8000/payment/callback/{}".format(
        event.user.id)
    userData = {
        'email': email,
        'amount': totalAmount,
        'reference': tx_ref,
        'callback_url': redirect_url,
        'metadata': json.dumps({'quantity': quantity, 'phone_number': phone_number, 'ticket_id': ticket_id})
    }
    headers = {
        "Authorization": f"Bearer {user_profile.secret_key}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(
            'https://api.paystack.co/transaction/initialize', headers=headers, json=userData)
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


def payment_callback(request, user_id):
    # Process the payment callback
    # print(user_id)
    owner = User.objects.get(id=user_id)
    owner = UserProfile.objects.get(user=owner)
    # print(owner.secret_key)
    response = request.GET
    reference = response['reference']
    # print(reference)
    headers = {
        "Authorization": f"Bearer {owner.secret_key}"
    }
    res = requests.get(
        'https://api.paystack.co/transaction/verify/{}'.format(reference), headers=headers)
    res = res.json()

    # print(res)

    status = res['data']['status']
    # # You can verify the payment status and update your database accordingly
    if status == 'success':
        ticket_id = res['data']['metadata']['ticket_id']
        amount = res['data']['amount']
        email = res['data']['customer']['email']
        phone_no = res['data']['metadata']['phone_number']
        quantity = res['data']['metadata']['quantity']
        transaction_id = res['data']['id']
        genCode = uuid.uuid4()
        code = str(genCode)
        amount = amount/100
        ticket = Ticket.objects.get(id=ticket_id)

        payment = Payment(
            ticket_id=ticket,
            price=amount,
            email=email,
            code=code,
            phone_no=phone_no,
            transaction_id=transaction_id
        )
        payment.save()
        if ticket is not None:
            event = ticket.event_id.name
            ticket.quantity_available = ticket.quantity_available - \
                int(quantity)
            ticket.save()
            sent_count = sendCodeToMail(
                email, event, amount, code, ticket.name, quantity)
            if sent_count == 1:
                # Email was sent successfully
                messages.success(
                    request, f"Payment successful, check your email: {email} for the ticket")
            else:
                # Email sending failed
                messages.error(request, "Failed to send email")
    #     messages.success(request, "Payment made successfully!")
    return redirect('/')


def send_email(request):

    genCode = uuid.uuid4()
    code = str(genCode)
    eventName = 'New Year Event'
    amountPaid = 2700
    ticketName = 'regular'
    Quantity = 1

    email = 'charlykso121@gmail.com'
    subject = 'Second one'
    message = "This is the second message"

    # generate QRCode
    byte_stream = GenerateCode.genQRCode(
        email, eventName, amountPaid, code, ticketName)

    # send mail message
    sent_count = SendMail.send_email_to_user(
        email, subject, message, byte_stream)
    if sent_count == 1:
        # Email was sent successfully
        messages.success(request, "Email sent successfully!")
    else:
        # Email sending failed
        messages.error(request, "Failed to send email")
    print(sent_count)
    return redirect('/')


def present(request, email, code):
    payment = Payment.objects.get(code=code)
    if payment.present == True:
        return HttpResponse('{} is already present'.format(payment.email))
    payment.present = True
    payment.save()
    return HttpResponse('You are welcome: {} and your code is {}'.format(email, code))
