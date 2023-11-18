# from django.shortcuts import render

# def confirm(request):
#     return render(request, 'confirm.html')  # Assuming your HTML code is in 'token_page.html'
# from django.shortcuts import render
# from django.core.mail import send_mail
# import secrets
# import string

# def generate_token(length=8):
#     characters = string.ascii_letters + string.digits
#     return ''.join(secrets.choice(characters) for _ in range(length))

# def send_token_email(email, token):
#     subject = 'Your Confirmation Token'
#     message = f'Your confirmation token is: {token}'
#     from_email = 'muwongeshanitaklarisha@gmail.com'  # Update with your email address
#     send_mail(subject, message, from_email, [email])

# def confirm(request):
#     if request.method == 'POST':
#         # Assuming you have a form with 'email' field in your template
#         email = request.POST.get('email')
#         token = generate_token()
#         send_token_email(email, token)
#         # Perform any other actions like saving the token or redirecting the user

#     return render(request, 'confirm.html')
