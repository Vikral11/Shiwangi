from django.shortcuts import render,HttpResponseRedirect
from django.conf import settings
from django.core.mail import send_mail
from .models import * 


# Create your views here.
def home(request):
    try:

    
        if (request.method=="POST"):
            m=mail()
            m.name=request.POST.get("contactName")
            gmail=m.email=request.POST.get("contactEmail")
            m.subject=request.POST.get("contactSubject")
            m.message=request.POST.get("contactMessage")
            m.save()
            subject = 'welcome to GFG world'
            message = (f"""Hi {contact.name},

                Thanks so much for reaching out! This auto-reply is just to let you know…

                I received your email and will get back to you as soon as possible. During [business_hours] that’s usually within a couple of hours. Evenings and weekends may take us a little bit longer.

                If you have general questions about me, check out our social media for walkthroughs.

                If you have any additional information that you think will help us to assist you, please feel free to reply to this email.

                We look forward to chatting soon!

                Cheers,

                Shiwangi Pandey""")
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [gmail, ]
            send_mail( subject, message, email_from, recipient_list )


            subject = 'Someone contacted'
            message = f'Hi Shiwangi, \n Name: {m.name} \n Email: {gmail}  \n Subject: {m.subject} \n Message: {m.message}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ["shiwipandey25@gmail.com" ]
            send_mail( subject, message, email_from, recipient_list )        
            return HttpResponseRedirect("/")

    finally:
        return render(request, "index.html")