import qrcode
import io
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

class GenerateCode:

    def genQRCode(email, eventName, amountPaid, code, ticketName, quantity ):
        # generate qrcode
        url = 'http://192.168.5.148:8000/payment/present/{}/{}/'.format(email, code)
        data = {
            'UserEmail' : email,
            'Event': eventName,
            'Amount': amountPaid,
            'SecretCode': code,
            'Ticket': ticketName,
            'Quantity': quantity,
            'url': url
        }

        # Generate the QR code image
        qr_code = qrcode.make(data)

        byte_stream = io.BytesIO()
        qr_code.save(byte_stream, format='PNG')

        # # Set the byte stream position to the beginning
        byte_stream.seek(0)

        # # Return the QR code image as a Django HttpResponse
        # response = HttpResponse(byte_stream, content_type="image/png")
        # return response
        return byte_stream
