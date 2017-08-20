from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from rating.models import *

# Create your views here.
def uploadImg(request):
    if request.method == 'POST':
        new_img = IMG(
            img=request.FILES.get('img')
        )
        new_img.save()
    return render(request, 'b/uploadimg.html')

def showImg(request):
    imgs = IMG.objects.all()
    content = {
        'imgs':imgs,
    }
    return render(request, 'b/showimg.html', content)

def register(request):
    if request.method=='POST':
        password=request.POST['Password1']
        password2=request.POST['Password2']
        firstname=request.POST['Firstname']
        lastname = request.POST['Lastname']
        email = request.POST['Email']
        username=firstname+'.'+lastname
        if password!=password2:
            return render(request,'register.html',{'error':'Passwords do not match!'})
        elif password==password2:
            User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=email)
            R_User.objects.create(user=User.objects.get(username=username))
            return render(request,'index.html')
    else:
        return render(request,'register.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST['Email']
        password = request.POST['Password']
        username = User.objects.get(email=email)
        user = authenticate(request,username=username.username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return render(request,'index.html')
            else:
                return render(request,'login.html',{'error':'Your account is disabled!Please contact our administrator.'})
        else:
            return render(request,'login.html',{'error':'Your email address or password was entered incorrectly.'})
    else:
        return render(request, 'login.html')

@login_required(login_url='/login')
def user_logout(request):
    logout(request)
    return render(request,'index.html')

def index(request):
    return render(request,'index.html')

def forgot_password(request):
    return render(request,'forgotpassword.html')

def index_content(request):
    return render(request,'Puzzles/index-content.html')

def detail(request):
    if request.method=='POST':
        username=request.user
        time=datetime.datetime.now()
        comment=request.POST['comment']
        Comment.objects.create(user=R_User.objects.get(user__username=username),article=Article.objects.get(title='Katy Perry'),time=time,text=comment)

    count=Comment.objects.filter(article__title='Katy Perry').count()
    comment=Comment.objects.filter(article__title='Katy Perry')
    try:
        article=Article.objects.get(title='Katy Perry')
    except:
        return render(request, 'detail.html',{'error':'No Data'})
    return render(request, 'detail.html',{'article':article,'count':count,'comment':comment})

def category(request):
    direction=['right','right','left','left']
    return render(request,'category.html',{'direction':direction})