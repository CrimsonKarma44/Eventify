from django.core.mail import send_mail
from django.conf import settings

class SendMail:

    def send_email_to_user(user_email, subject, message):
        print(user_email)
        sent_count = send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user_email],
            fail_silently=False,
        )

        if sent_count == 1:
            # Email was sent successfully
            print("Email sent successfully!")
        else:
            # Email sending failed
            print("Failed to send email!")

        return sent_count
