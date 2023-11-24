import pyotp
from datetime import datetime, timedelta
from django.core.mail import send_mail 
from pyotp.utils import random_base32

def send_otp(request):
    token = pyotp.TOTP(random_base32(), interval=60)
    token_input = token.now()
    request.session['token_secret_key'] = token.secret
    valid_date = datetime.now() + timedelta(minutes=1)
    request.session['token_input_valid_date'] = str(valid_date)

    print(f'Your OTP is {token_input}')
    # # Send token to user via email    
    # subject = 'OTP for login'
    # message = f'Your OTP for login is {token.now()}'
    # email_from = settings.EMAIL_HOST_USER
    # recipient_list = [request.user.email]
    # send_mail(subject, message, email_from, recipient_list)


    