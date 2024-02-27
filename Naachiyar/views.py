from django.shortcuts import render ,redirect
from django.http import HttpResponse
from . models import user,Contact,Quote,Job,Worker

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST ['password']
        users=user(username=username,email=email,password=password)
        users.save()
        return redirect('Naachiyar:login')
    return render(request,"login.html")


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email and password:  # Check if email and password are provided
            try:
                users = user.objects.get(email=email, password=password)
                request.session['email'] = email
                request.session.set_expiry(28800)
                return redirect('Naachiyar:home')
            except user.DoesNotExist:
                error = 'Incorrect Email/Password'
        else:
            error = 'Please provide both email and password'
        return render(request, "login.html", {'error': error})
    else:
        if 'email' in request.session:
            return redirect('Naachiyar:home')
        else:
            return render(request, "login.html")
        
def home(request):
    return render (request,"index.html")

def contact(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get("name")
        email=request.POST.get("email")
        subject=request.POST.get("subject")
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()
        return render(request,"index.html")
    return render(request,"contact.html")

def quote(request):
    if request.method=="POST":
        quote=Quote()
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        description=request.POST.get("description")
        budget=request.POST.get("budget")
        s_date=request.POST.get("s_date")
        e_date=request.POST.get("e_date")
        location=request.POST.get("location")
        quote.name=name
        quote.email=email
        quote.phone=phone
        quote.description=description
        quote.budget=budget
        quote.s_date=s_date
        quote.e_date=e_date
        quote.location=location
        quote.save()
        return render(request,"index.html")
    return render(request,"quote.html")

def job(request):
    if request.method=="POST":
        job=Job()
        name=request.POST.get("name")
        age=request.POST.get("age")
        email=request.POST.get("email")
        mobile=request.POST.get("mobile")
        role=request.POST.get("role")
        experience=request.POST.get("experience")
        city=request.POST.get("city")
        pincode=request.POST.get("pincode")
        date=request.POST.get("date")
        job.name=name
        job.email=email
        job.age=age
        job.mobile=mobile
        job.role=role
        job.experience=experience
        job.city=city
        job.pincode=pincode
        job.date=date
        job.save()
        return render(request,"index.html")
    return render(request,"job.html")

def admin(request):
    return render (request,"admin.html")

def worker(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        contact = request.POST.get("contact")
        designation = request.POST.get("designation")
        
        worker = Worker(name=name, age=age, contact=contact, designation=designation)
        worker.save()
        
        workers = Worker.objects.all()
        return render(request, "workers.html", {'workers': workers})
    
    return render(request, "workers.html")


def demo(request):
    workers = Worker.objects.all()
    return render(request,"workers.html", {'workers': workers})


    

