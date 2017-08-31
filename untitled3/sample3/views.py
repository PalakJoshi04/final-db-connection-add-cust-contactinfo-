from django.shortcuts import render
from .models import Customer
from .forms import CustomerForm


def index(request):
    return render(request, "index.html")


def people(request):
    form = CustomerForm()

    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            p = Customer()
            p.first_name = form.cleaned_data["first_name"]
            p.last_name = form.cleaned_data["last_name"]
            p.mobileNumber = form.cleaned_data["mobileNumber"]
            p.phoneNumber = form.cleaned_data["phoneNumber"]
            p.emailID = form.cleaned_data["emailID"]
            p.address1 = form.cleaned_data["address1"]
            p.address2 = form.cleaned_data["address2"]
            p.city = form.cleaned_data["city"]
            p.state = form.cleaned_data["state"]
            p.landmark = form.cleaned_data["landmark"]
            p.pincode = form.cleaned_data["pincode"]
            p.save()

        else:
            form = CustomerForm()

    po = Customer.objects.all()
    return render(request, "people.html", {"people": po, "form": form})
