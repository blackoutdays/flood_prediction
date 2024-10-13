from django.core.mail import send_mail
from django.conf import settings

# def send_sms(to_number, message):
#     # Реализуйте вашу логику для отправки SMS
#     pass
#
# def send_webhook_notification(url, data):
#     import requests
#     response = requests.post(url, json=data)
#     return response.status_code