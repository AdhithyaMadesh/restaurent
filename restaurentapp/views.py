from django.shortcuts import render
from .models import submit
from django.http import HttpResponse
from django.core.mail import send_mail
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def hotel(request):
    return render(request, "hotel.html")

def submit_form(request):
    if request.method == "POST":
        name=request.POST.get("txtname")
        people=request.POST.get("txtpeople")
        mobile=request.POST.get("txtphone")
        time=request.POST.get("txttime")
        date=request.POST.get("txtdate")
        mail=request.POST.get("txtemail")
        result=submit(Name=name, People=people, Mobile=mobile, Time=time, Date=date, Mail=mail)
        result.save()
        
        send_mail("Reservation Confirmation at Royate",
                  "Thank you for choosing Royate for your upcoming dining experience.We are delighted to confirm your reservation. We appreciate your trust in our restaurant and are thrilled to have the opportunity to serve you.",
                  "madeshauto64@gmail.com",
                  [mail],
                  fail_silently=False)
        return render(request, "index.html")

        
    