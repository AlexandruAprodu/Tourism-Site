from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    return render(request, 'tinfo/index.html')


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message_name']
        mail = request.POST['mail']
        subject = request.POST['subject']
        send_mail(
            'Informatii despre produse: ' + message_name,  # subiect
            subject,  # mesaj
            mail,  # from email
            ['testingsiteromania@gmail.com'],  # to email
        )
        return render(request, 'tinfo/contact.html', {'message_name': message_name})
    else:
        return render(request, 'tinfo/contact.html', {'title': 'Contact'})
