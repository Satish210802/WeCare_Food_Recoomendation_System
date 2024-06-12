from django.shortcuts import render ,HttpResponse,redirect,HttpResponseRedirect
import pandas as pd
import os
from foodrec.settings import BASE_DIR
from recommender.functions import Weight_Gain ,Weight_Loss,Healthy, calculate_bmr, chatfunction, get_image
from recommender.models import Food,UserList
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        val = request.POST.get('val')
        if val == "1" :
            username1 = request.POST.get('user', None)
            password1 = request.POST.get('pass', None)
            # user1 = UserList.objects.all()
            user  = authenticate(username = username1, password= password1)
            if user is not None:
                login(request,user)
                messages.info(request, "Login Sussecfully")
                return redirect('home')

            # for data in user1:
            #     if (username == data.Username):
            #         pass1 = UserList.objects.all()
            #         for data in pass1:
            #             if (password == data.Password):
            #                 return redirect('home')
            messages.error(request, "Invalid username or password")
            context = {
                "notification":True
            }
            return render(request, 'login.html',context)
        else:
            username = request.POST.get('user1', None)
            password = request.POST.get('pass1', None)
            user_mail_id = request.POST.get('mail1',None)
            print(username)
            print(password)
            print(user_mail_id)
            if(UserList.objects.filter(mail_id1 = user_mail_id)).exists():
                print("USER EXISTED")
            else:
                new_user = UserList.objects.create(Username = username,Password = password,mail_id1 = user_mail_id)
                new_user.save()
                new_user1 = User.objects.create_user(username, user_mail_id, password)
                new_user1.save()
                messages.success(request, " Your iCoder has been successfully created")
                return redirect('home')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))
def index(request):
    if request.method=="POST":
        #df=pd.read_csv(os.path.join(BASE_DIR ,"static/data/newfood.csv"))
        #df=df.to_numpy()
        #for d in df:
        #    s=Food(name=d[0],bf=d[1],lu=d[2],di=d[3],cal=d[5],fat=d[6],pro=d[7],sug=d[15],imagepath=d[16])
        #    s.save() 
        age=int(request.POST.get("age"))
        # veg=int(request.POST.get("veg/nonveg"))
        weight=int(request.POST.get("weight"))
        height=int(request.POST.get("height"))
        bodyfat=float(request.POST.get("bodyfat"))
        goal=request.POST.get("goal")
        activity=(request.POST.get("activity"))
        gender=request.POST.get("gender")
        category = request.POST.get("cat")
        bmr = calculate_bmr(weight,height,age,gender,activity,category)
        print(bmr)
        maintaincalories=int(bmr)
        
        caloriesreq=0
        finaldata=[]
        bmi=0
        bmiinfo=""
        if(goal=="weight gain"):
            print("wg")
            finaldata=Weight_Gain(age,weight,height)
            bmi=int(finaldata[len(finaldata)-2])
            bmiinfo=finaldata[len(finaldata)-1]
            caloriesreq=maintaincalories+400
        if(goal=="weight loss"):
            print("wl")
            finaldata=Weight_Loss(age,weight,height)
            bmi=int(finaldata[len(finaldata)-2])
            bmiinfo=finaldata[len(finaldata)-1]
            caloriesreq=maintaincalories-750
        
        if(goal=="healthy"):
            print("h")
            finaldata=Healthy(age,weight,height)
            bmi=int(finaldata[len(finaldata)-2])
            bmiinfo=finaldata[len(finaldata)-1]
            caloriesreq=maintaincalories
        # else:
        #     print("wrong choice")
  
        breakfastdata=Food.objects.all().filter(bf=1).filter(name__in=finaldata)
        lunchdata=Food.objects.all().filter(lu=1).filter(name__in=finaldata)
        dinnerdata=Food.objects.all().filter(di=1).filter(name__in=finaldata)


        # print(finaldata,"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        context={
            "breakfast":breakfastdata,
            "lunch":lunchdata,
            "dinner":dinnerdata,
            "bmi":bmi,
            "bmiinfo":bmiinfo,
            "caloriesreq":caloriesreq
        }

        return render(request,"diet.html",context)


    return render(request,"index.html")


def bodymass(request):
    return render(request,"bodymass.html")   

def home(request):

    return render(request,"home.html")        

# def login(request):
#     return render(request,"login.html")

def diet(request):
    return render(request,"diet.html")

def Dashboard(request):
    if request.method == "POST":
        Question = request.POST.get("Question")
        ans = chatfunction(Question)
        getimg = get_image(Question)
        context = {
            "Question": ans,
        }
        return render(request,"information_gain.html",context)
    return render(request, "information_gain.html")

def satish(request):
    return render(request,"satish.html")

def koustubh(request):
    return  render(request,"koustubh.html")

def sagar(request):
    return  render(request,"sagar.html")
def saurabh(request):
    return  render(request,"saurabh.html")
def team(request):
    return  render(request,"team.html")
def contact(request):
    return render(request,"contact.html")
def profile(request):
    return render(request,"dash/dashboard.html")