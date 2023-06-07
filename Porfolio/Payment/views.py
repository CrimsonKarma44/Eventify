from django.shortcuts import render
import requests
from django.http import HttpResponse

# Create your views here.
def payment(request):
    return render(request, 'payment.html')

def make_payment(request):
    # Collect the necessary payment details from the request
    amount = 5000  # Example amount
    email = "example@example.com"  # Example email

    # Set up the request payload
    payload = {
        "tx_ref": "unique_transaction_reference",
        "amount": amount,
        "currency": "NGN",
        "redirect_url": "http://your-website.com/payment/callback",
        "payment_options": "card",
        "customer": {
            "email": email
        },
        "customizations": {
            "title": "Payment for Order XYZ",
            "description": "Payment for items purchased on your-website.com",
        }
    }

    # Make a POST request to Flutterwave's payment initiation endpoint
    headers = {
        "Authorization": "Bearer FLWSECK_TEST-6f6ed5664336aaf1ae5ee6c28f5446d9-X",
        "Content-Type": "application/json"
    }
    response = requests.post('https://api.flutterwave.com/v3/payments', json=payload, headers=headers)

    # Process the response
    if response.status_code == 200:
        data = response.json()
        return HttpResponse(data['data']['link'])
    else:
        return HttpResponse("Error occurred during payment initiation.")


def payment_callback(request):
    # Process the payment callback
    # You can verify the payment status and update your database accordingly

    return HttpResponse("Payment callback received.")
