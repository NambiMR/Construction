from django.shortcuts import render ,redirect
from django.http import HttpResponse
from . models import user,Contact,Quote,Job,Worker,Project,Feedback

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
def projects(request):
    return render (request,"projects.html")

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



def feedback(request):
    if request.method=="POST":
        feedback=Feedback()
        Name=request.POST.get("Name")
        Email=request.POST.get("Email")
        Age=request.POST.get("Age")
        Phone=request.POST.get("Phone")
        Message=request.POST.get("Message")
        Rate=request.POST.get("Rate")
        feedback.Name=Name
        feedback.Email=Email
        feedback.Age=Age
        feedback.Phone=Phone
        feedback.Message=Message
        feedback.Rate=Rate
        feedback.save()
        return render(request,"index.html")
    return render(request,"feedback.html")

def admin(request):
    return render (request,"admin.html")


from django.shortcuts import render, redirect
from .models import Worker,Project

def show_workers(request):
    workers = Worker.objects.all()
    return render(request, "workers.html", {'workers': workers})

def add_worker(request):
    if request.method == "POST":
        worker = Worker()

        name = request.POST.get("name")
        age = request.POST.get("age")
        contact = request.POST.get("contact")
        designation = request.POST.get("designation")

        
        worker = Worker(name=name, age=age, contact=contact, designation=designation)
        worker.save()
        
        workers = Worker.objects.all()
        return render(request, "workers.html", {'workers': workers})
    
    return render(request, "workers.html")

def show_project(request):
    project = Project.objects.all()
    return render(request, "project.html", {'project': project})

def delete_project (request , id):
    project=Project.objects.get(id=id)
    project.delete()
    return redirect("/show_project")

def add_project(request):
    if request.method == "POST":
        project = Project()
        project_name = request.POST.get("pname")
        client_name = request.POST.get("cname")
        contact = request.POST.get("contact")
        location = request.POST.get("location")
        budget = request.POST.get("budget")
        sdate = request.POST.get("sdate")
        status = request.POST.get("status")
        edate = request.POST.get("edate")
        print(project_name,client_name,contact)
        project = Project(project_name=project_name, client_name=client_name, contact=contact, location=location, budget=budget, sdate=sdate, status=status, edate=edate)
        project.save()
        
        project = Project.objects.all()
        return render(request, "project.html", {'project': project})
    print("page load")
    return render(request, "project.html")




def Feedback_show(request):
    feedback= Feedback.objects.all()
    return render(request, "adminfeedback.html", {'feedback': feedback})

def Quote_show(request):
    quote= Quote.objects.all()
    return render(request, "adminquote.html", {'quote': quote})

def footer(request):
    return render(request,'footer.html')