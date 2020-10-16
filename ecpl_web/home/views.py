from django.shortcuts import render,redirect
from .models import Services,Testimonials,Contactform,Team,Clients,Careers,Candidate
from . import forms
from django.contrib import messages

def index(request):
    services = Services.objects.all()
    testimonials=Testimonials.objects.all()
    clients = Clients.objects.all()
    form=forms.QuickContact()
    data = {'services': services,'testimonials':testimonials,'clients':clients,'form':form}
    return render(request,'index.html',data)

def contact(request):
    return render(request,'contact.html')

def aboutus(request):
    team=Team.objects.all()
    testimonials = Testimonials.objects.all()
    clients=Clients.objects.all()
    form = forms.QuickContact()
    data={'teams':team,'testimonials':testimonials,'clients':clients,'form':form}
    return render(request,'about.html',data)

def add_message(request):
    message=request.POST['message']
    name=request.POST['name']
    email=request.POST['email']
    subject=request.POST['subject']
    contact=Contactform(message=message,name=name,email=email,subject=subject)
    contact.save()
    return render(request,'index.html')

def claim_processing(request):
    return render(request,'claim_processing.html')

def pi_request(request):
    return render(request,'PI_request.html')
def order_taking(request):
    return render(request,'order_taking_service.html')
def certification(request):
    return render(request,'certification.html')
def infra(request):
    return render(request,'infra.html')

def careers(request):
    career = Careers.objects.all()
    data={'careers':career}
    return render(request,'careers.html',data)

def career_view(request,pid):
    career = Careers.objects.get(id=pid)
    data = {'careers': career}
    return render(request,'career_view.html',data)

def add_candidate(request):

    name=request.POST['name']
    email=request.POST['email']
    phone=request.POST['phone']
    resume = request.POST['resume']
    candidate=Candidate(name=name,email=email,phone=phone,resume=resume)
    candidate.save()
    return render(request,'index.html')

def all_services(request):
    services = Services.objects.all()
    data = {'services': services}
    return render(request,'services.html',data)

def addcontact(request):
    if request.method == 'POST':
        form=forms.QuickContact(request.POST)
        if form.is_valid():
            #saving
            instance=form.save(commit=False)
            instance.save()
            messages.info(request,'Contact Added')
            print('Saved')
        return redirect('/')
    else:
        form = forms.QuickContact()
        return render(request,'index.html', {'form': form})

