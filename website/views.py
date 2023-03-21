from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect
from website.models import Member
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import ResumeForm
from website.models import Resume
from django.views import View


# from django.shortcuts import render
# from .forms import UploadFileForm
# # from somewhere import handle_uploaded_file

from django.contrib.auth.models import User , auth

# Create your views here.
def index(request):
    return HttpResponse("this is home page")

def services(request):
    return render (request, )
    

def home(request):
    return render(request,'home.html',{}) 
    messages.success(request, 'Profile details updated')   

 
def register(request):
    if request.method == 'POST' :
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        skills =request.POST.get('skills')
        CTC =request.POST.get('CTC')
        Experience =request.POST.get('Experience')
        age = request.POST.get('age')
        upload=request.POST.get('upload')
        register = Member(fname=fname, lname=lname, email=email, age=age,skills=skills,CTC=CTC,Experience=Experience,resume=upload)
        register.save()
        print("form submitted")
        messages.success (request, 'Profile details updated')
        return render(request,'home.html')   
    # messages.add_message(request, messages.INFO, 'Hello world.')
        # messages.success (request, 'Profile details updated')
    return render(request,'register.html')    


class HomeView(View):
    def get(self, request):
        form = ResumeForm()
        return render(request,'register.html', {"form":form})   

def SaveProfile(request):
   saved = False
   
   if request.method == "POST":
      #Get the posted form
      MyProfileForm = ResumeForm(request.POST, request.FILES)
      
      if MyProfileForm.is_valid():
         profile = Resume()
         profile.fname = MyProfileForm.cleaned_data["fname"]
         profile.lname = MyProfileForm.cleaned_data["lname"]
         profile.email = MyProfileForm.cleaned_data["email"]
         profile.skills = MyProfileForm.cleaned_data["skills"]
         profile.CTC = MyProfileForm.cleaned_data["CTC"]
         profile.Experience = MyProfileForm.cleaned_data["Experience"]
         profile.age = MyProfileForm.cleaned_data["age"]
         profile.resume = MyProfileForm.cleaned_data["resume"]
         profile.save()
         saved = True
         messages.success (request, 'Profile details updated')
         return render(request,'home.html')   
   else:
      MyProfileForm = ResumeForm()
		
   return render(request, 'register.html' ) 

    

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadFileForm()
#     return render(request, 'upload.html', {'form': form})


def loginuser(request):
    print('##############!!!!!!!!!')
    if request.method == 'POST' :
       username = request.POST.get('username')
       password = request.POST.get('password')
      # print('##############!!!!!!!!!')

       user = authenticate(username='username', password='password')

       if user is not None:
        # A backend authenticated the credentials
         login(request,user)
         return redirect ("/info.html")
       else:
         # No backend authenticated the credentials
          return render(request,'login.html',{})

        
    return render(request,'login.html',{})

def Contactus(request):
    if request.user.is_anonymous:
         return redirect("/login.html")
    return render(request,'Contactus.html')

def logoutuser(request):
    logout(request)
    return redirect("/login")
 
def whoAreWe(request):
    if request.user.is_anonymous:
         return redirect("/home.html")
    return render(request,'who.html')
def WeDo(request):
    if request.user.is_anonymous:
         return redirect("/home.html")
    return render(request,'weDo.html')

def sustainability(request):
    if request.user.is_anonymous:
         return redirect("/home.html")
    return render(request,'sustainability.html')

def investor(request):
    if request.user.is_anonymous:
         return redirect("/home.html")
    return render(request,'investor.html')
def career(request):
    if request.user.is_anonymous:
         return redirect("/home.html")
    return render(request,'career.html')