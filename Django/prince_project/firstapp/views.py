from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse
from .models import *
# import re 
# def home (request):
    # return HttpResponse("""
#                         <br><br><br><br><br>
# <center>
# <br>
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

# <table  border="1">

# 	<tr>
# 		<th>  Image  </th>
# 		<th>  Text  </th>
# 	</tr>
# 	<tr>
# 		<td>  <img src ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCZHeOeTJ3UVPCVUlgN1BmTn0KUNcCRvDsYQ&s"  width ="10%">    </td>
# 		<td> <h1> Prince Kumar </h1> </td>
# 	</tr>
#  </table>
#  </center>
#  </b>""")

def home (request):
    if request.method=='POST':
           data = request.POST
           emp_name = data.get("Emp_name")
           emp_email = data.get("Emp_Email")
           emp_mobile = data.get("Emp_Mobile")

           print(emp_name)
           print(emp_email)
           print(emp_mobile)

           Employee.objects.create(
                Emp_name = emp_name,
                Emp_Email = emp_email,
                Emp_Mobile = emp_mobile
            )
           return redirect('/')

    quary = Employee.objects.all()
    context = {'employee':quary}
    return render(request,"index.html",context)

def delete(request,id):
     quary_delete = Employee.objects.get(id=id)
     quary_delete.delete()
     return redirect("/")        
def update (request, id):
    if(request.method=="POST"):
        data = request.POST
        emp_name = data.get("Emp_name")
        emp_email = data.get("Emp_Email")
        emp_mobile = data.get("Emp_Mobile")
        Employee.objects.filter(id=id).update(
            Emp_name = emp_name,
            Emp_Email = emp_email,
            Emp_Mobile = emp_mobile
           )
        return redirect('/')

    query1=Employee.objects.get(id=id)
    context={"emp_update": query1}
    return render(request,"update.html", context)

def success (request):
    return HttpResponse("<h1> Success Page </h1>")

def success1 (request):
    return render (request , "success.html")
def login1(request):
    if request.method == 'POST':
        data1 = request.POST
        username = data1.get("username")
        userpassword = data1.get("password")
        loginuser = authenticate(request, username=username, password=userpassword)
        if loginuser is not None:
            login(request, loginuser)
            return redirect('homeafterlogin')
        else:
            return HttpResponse("Username or password may be WRONG.")
    return render(request, "login.html")
def signup1(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get("username")
        useremail = data.get("email")
        userpassword1 = data.get("password1")
        userpassword2 = data.get("password2")
        if userpassword1 != userpassword2:
            return HttpResponse("The passwords are mismatched")

        createuser = User.objects.create_user(username=username,email=useremail,password=userpassword1)
        createuser.save()
        return redirect('login1')
    return render(request, "signup.html")
def logoutpage(request):
     logout(request)
     return redirect ('login1')

@login_required
def homeafterlogin(request):
    return render (request , "homeafterlogin.html")

def blog(request):
    if request.method == 'POST':
        form_btext = request.POST.get("btext")
        form_bdate = request.POST.get("bdate")
        form_btime = request.POST.get("btime")
        form_bimage = request.FILES.get("bimage")
        Blog.objects.create(
            btext = form_btext,
            bdate = form_bdate,
            btime = form_btime,
            bimage = form_bimage
        )
        return redirect('/blog/')
    query = Blog.objects.all()
    context = {'blogdata': query}
    return render(request, "blog.html", context)
