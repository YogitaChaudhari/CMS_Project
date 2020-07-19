from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import User,Complaint
from myapp.form import UserForm,ComplaintForm
# Create your views here.
def indexpage(request):
    eid=request.session.get("email")
    il=Complaint.objects.filter(email_id=eid)
    return render(request,'index.html',{'il':il})

def homepage(request):
    return render(request,'home.html')

def About(request):
    return render(request,'about.html')

def Contact(request):
    return render(request,'contact.html')

def adduserpage(request):
    u= UserForm
    return render(request, 'adduser.html',{'form':u})

def adduser(request):
    u= UserForm(request.POST)
    if u.is_valid:
        u.save()
        return render(request,'index.html')
    return HttpResponse("<h1>Fail</h1")

def userlist(request):
    l= User.objects.all()
    return render(request,'userlist.html',{'form1':l})

def deleteUser(request,email):
    d= User.objects.get(email=email)
    d.delete()
    return render(request,'index.html')

def editUser(request):
    email=request.GET.get('email')
    em=User.objects.get(email=email)
    uf=UserForm(instance=em)
    return render(request,'update.html',{'form1':uf,'email':email})

def updateUser(request):
    email=request.GET.get('email')
    up=User.objects.get(email=email)
    us=UserForm(request.POST,instance=up)
    us.save()
    return redirect("/userlist")

def addcomplaintpage(request):
    c= ComplaintForm
    return render(request,'complaint.html',{'form2':c})

def addcomplaint(request):
    c= ComplaintForm(request.POST)
    if c.is_valid:
        c.save()
        return render(request,'index.html')
    return HttpResponse("<h1>FAIL</h1>")

def complaintlist(request):
    y= Complaint.objects.all()
    return render(request,'complaintList.html',{'form3':y})

def addsignUpPage(request):
    f= UserForm
    return render(request,'signUp.html',{'su':f})

def signUp(request):
    f= UserForm(request.POST)
    if f.is_valid:
        f.save()
        return render(request,'index.html')
    return HttpResponse("<h1>FAIL</h1>")

def addloginpage(request):
    return render(request,'loginpage.html')


def login(request):
    em=request.POST.get('email')
    passwd=request.POST.get('password')
    if em=="yogita@123" and passwd=="123":
        request.session['adminName']=em
        return render(request, 'navbar.html')    
    else:
        try:
            su=User.objects.get(email=em)
            if em==su.email and passwd==su.password:
                request.session['username']=em
                return render(request,'navbar.html') 
            else:
                return HttpResponse("Template Does Not Exist")
        except:
            return render(request,'loginpage.html')

def LogOut(request):
    ls=list(request.session.keys())
    for i in ls:
        del request.session[i]
    return render(request,'index.html')


def deleteComplaint(request,id):
    c=Complaint.objects.get(id=id)
    c.delete()
    return redirect("/complaintlist")

def editComplaint(request):
    id=request.GET.get('id')
    ed=Complaint.objects.get(id=id)
    x=ComplaintForm(instance=ed)
    return render(request,'updateComplaint.html',{'form':x,'id':id})


def updateComplaint(request):
    id=request.GET.get('id')
    ed=Complaint.objects.get(id=id)
    x=ComplaintForm(request.POST,instance=ed)
    x.save()
    return redirect("/complaintlist")


def userComplaint(request):
    eid=request.session.get("email")
    il=Complaint.objects.filter(email_id=eid)
    q={'incl':il}
    return render(request,'userComplaint.html',q)

def editProfilepage(request):
    return render(request,'editProfile.html')
    
def editProfile(request): 
    email=request.GET.get('email')
    ep=User.objects.get(email=email)
    s=UserForm(instance=ep)
    return render(request,'updateProfile.html',{'form5':s,'email':email})

def updateProfile(request):
    email=request.GET.get('email')
    ep=User.objects.get(email=email)
    s=UserForm(request.POST,instance=ep)
    s.save()
    return redirect("/editProfile")

