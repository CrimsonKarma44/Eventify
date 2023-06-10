from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage

class SendMail:

    def send_email_to_user(user_email, subject, message, byte_stream):
        
        try:
            message = EmailMessage(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [user_email],
            )

            message.attach('qr_code.png', byte_stream.getvalue(), "image/png")

            sent_count = message.send(fail_silently=False)
            return sent_count
        except Exception as e:
            error_message = str(e)
            print(error_message)
            sent_count = 0
            return sent_count
