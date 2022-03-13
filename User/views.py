from django.shortcuts import render,redirect
from .models import User

def addUserPage(request):
    try:
        return render(request,"addUser.html")
    except:
        return redirect("/")

def addUser(request):
    try:
        data=request.POST
        emailid=data['emailid']
        number=data['mobilenumber']
        status=False
        if(User.objects.filter(emailid=emailid)):
            msg="Email Id Already Exist"
        elif(User.objects.filter(phonenumber=str(number))):
            msg="Mobile Number Already Exist"
        else:
            obj=User()
            obj.name=data['name']
            obj.emailid=emailid
            obj.phonenumber=number
            obj.address=data['address']
            obj.dateofbirth=data['dateofbirth']
            obj.username=data['username']
            obj.save()
            status=True
            msg="User Add Success Full"
        return render(request,"addUser.html",{"msg":msg,"status":status})
    except Exception as e:
        print(e)
        return render(request,"addUser.html",{"msg":"Server Error...","e":e})


def showUser(request):
    try:
        data=User.objects.all()
        return render(request,"listUser.html",{"data":data})
    except:
        return redirect("/")