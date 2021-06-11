from datetime import timezone
from django.shortcuts import render
from contact_forms.models import Form
from django.http import HttpResponse

# renders the home.html
def homePage(request):
    return render(request, "home.html")

# render the services.html
def services(request):
    return render(request, "services.html")

# render the about.html
def about(request):
    return render(request, "about.html")

# render the contact.html
def contact(request):
    return render(request, "contact.html")

def contact_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        e_mail = request.POST['e_mail']
        subject = request.POST['subject']
        service = request.POST['service']
        message = request.POST['message']
        new_form = Form(name=name, e_mail=e_mail, subject=subject, service=service, message=message)
        new_form.save(force_insert=True)

        return HttpResponse('')
    