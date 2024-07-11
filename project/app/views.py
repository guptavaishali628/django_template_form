from django.shortcuts import render
from .models import Student
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'app/home.html')

def register(request):
    name=request.POST.get('name')
    email=request.POST.get('email')   
    contact=request.POST.get('contact')
    password=request.POST.get('password')
    cpassword=request.POST.get('cpassword') 
    
    #validations in register form============>
    data=Student.objects.filter(Email=email)
    if data:
        msg='Email already exist'
        return render(request,'app/home.html',{'key':msg})
    else:
        if password==cpassword:
            Student.objects.create(Name=name, Email=email,Contact=contact,Password=password)
            msg='registration successfully!'
            return render(request,'app/home.html',{'key':msg})
        
        #return HttpResponse("registration successfully")

        else:
           msg="password and cpassword do not matched!"
           return render(request,'app/home.html',{'key':msg})
           
    # print(name)
    # print(email)
    # print(contact)
    # print(password)  
    
    # Student.objects.create(Name=name, Email=email,Contact=contact,Password=password)
    # return HttpResponse("registration successfully")

def login(request):
    return render(request,'app/login.html')

def logindata(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        # print(email,password)
        user=Student.objects.filter(Email=email)
        if user:
            data=Student.objects.get(Email=email)
            passs=data.Password
            print(passs)

            

    
    
    
    
    # print(request.method)
    # print(request.POST)
    # return HttpResponse("successfully done!")