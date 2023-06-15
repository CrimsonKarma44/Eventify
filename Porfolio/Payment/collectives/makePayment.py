import requests

def initiate_payment(event, userData):
    # flutterwave_account = event.owner.flutterwaveaccount

    payload = {
        "tx_ref": "unique-transaction-reference",
        "amount": userData['totalAmount'],
        "currency": "NGN",
        "payment_options": "card",
        "redirect_url": 'http://127.0.0.1:8000/payment/callback/',
        "customer": {
            "email": userData['email'],
            "phone_number": userData['phone_number'],
        },
        "meta": {
            "event_id": event.id,
        },
        "customizations": {
            "title": event.name,
            "description": event.description,
            # Customize other parameters as needed
        }
    }

    headers = {
        "Authorization": "Bearer FLWPUBK_TEST-42fdb47d708e442d1d3d288c10e5c4be-X",
        "Content-Type": "application/json",
    }

    response = requests.post(
        "https://api.flutterwave.com/v3/payments",
        json=payload,
        headers=headers,
    )
    print("Status Code:", response.status_code)
    response_data = response.json()
    print("Response:", response_data)
    return response
