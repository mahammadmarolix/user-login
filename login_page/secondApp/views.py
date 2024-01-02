from django.shortcuts import render,redirect

# Create your views here.
from . models import Login
from django.contrib.auth.models import auth
from django.http import HttpResponse

# Create your views here.
def register_page(request):
    if request.method =="POST":
        euser_name = request.POST['user_name']
        efirst_name = request.POST['first_name']
        elast_name = request.POST['last_name']
        eemail = request.POST['email']
        epassword = request.POST['password']
        econform_password = request.POST['conform_password']

        a = Login(user_name=euser_name,first_name=efirst_name,last_name=elast_name,email=eemail,password=epassword,conform_password=econform_password)
        a.save()
        if econform_password != econform_password:
            return HttpResponse("invalid details")
        else:

            return redirect('login')
        
    return render(request,'register.html')


def login_page(request):
    if request.method == "POST":
        nuser_name = request.POST['user_name']
        npassword = request.POST['password']
        # c = auth.authenticate (user_name = buser_name,password = bpassword)
        # if c is not None:
        #     auth.login(request.c)
        #     # return redirect('home')
        # else:
        #     return HttpResponse("Username or Password  is incorrect!!!!!")
        signup = Login.objects.all()
        user = None
        for i in signup:
            if (i.user_name,i.password) == (nuser_name,npassword):
                user = i.user_name
                request.method = ""
                break
        if user is not None:
            return redirect("home")
        else:
            return HttpResponse("Invaild Login details")
    return render(request,"login.html")





def home_page(request):
    if request.method=='POST':
        return redirect('login')
    return render(request,'home.html')