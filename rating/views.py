from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from rating.models import *
import math
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
            user=authenticate(request,username=username,password=password)
            login(request,user)
            return HttpResponseRedirect('index.html')
    else:
        return render(request,'register.html')

def user_login(request):
    if request.method == 'POST':
        try:
            email = request.POST['Email']
            password = request.POST['Password']
            username = User.objects.get(email=email)
            user = authenticate(request,username=username.username, password=password)
            login(request, user)
            profile = R_User.objects.get(user__username=user)
            return HttpResponseRedirect('index')

        except:
            return render(request,'login.html',{'error':'Your email address or password was entered incorrectly.'})
    else:
        return render(request,'login.html')

@login_required(login_url='/login')
def user_logout(request):
    logout(request)
    return render(request,'index.html')

def index(request):
    content=Article.objects.all().order_by('?')[:8]
    banner1=Article.objects.get(title='Katy Perry')
    banner2 = Article.objects.get(title='Ben Whishaw')
    banner3 = Article.objects.get(title='Jon Kortajarena')
    return render(request,'index.html',{'content':content,'banner1':banner1,'banner2':banner2,'banner3':banner3})

def forgot_password(request):
    return render(request,'forgotpassword.html')

def index_content(request):
    return render(request,'Puzzles/index-content.html')

def detail(request,name):
    if request.method=='POST':
        try:
            username=request.user
            time=datetime.datetime.now()
            comment=request.POST['comment']
            Comment.objects.create(user=R_User.objects.get(user__username=username),article=Article.objects.get(title__iexact=name),time=time,text=comment)
            request.COOKIES.clear()
            return HttpResponseRedirect('detail-'+name)
        except:
            pass
        try:
            cc1 = int(request.POST['c1'])
            cc2 = int(request.POST['c2'])
            cc3 = int(request.POST['c3'])
            cc4 = int(request.POST['c4'])
            cc5 = int(request.POST['c5'])
            aavg = request.POST['avg_mark']
            users = Article.objects.get(title__iexact=name).users
            c1=((Article.objects.get(title__iexact=name).C1)*users+cc1)/(users+1)
            c2 = ((Article.objects.get(title__iexact=name).C2) * users + cc2) / (users + 1)
            c3 = ((Article.objects.get(title__iexact=name).C3) * users + cc3) / (users + 1)
            c4 = ((Article.objects.get(title__iexact=name).C1) * users + cc4) / (users + 1)
            c5 = ((Article.objects.get(title__iexact=name).C1) * users + cc5) / (users + 1)
            avg =Decimal((c1+c2+c3+c4+c5)/5)
            users = users+1
            Article.objects.filter(title__iexact=name).update(C1=c1, C2=c2, C3=c3, C4=c4, C5=c5, AVG=avg,users=users)
            return HttpResponseRedirect('detail-' + name)
        except:
            pass

    else:
        pass

    count=Comment.objects.filter(article__title__iexact=name).count()
    comment=Comment.objects.filter(article__title__iexact=name).order_by('-time')
    sidebar2=Article.objects.all().order_by('?')[:3]
    sidebar=sidebar2
    try:
        article=Article.objects.get(title__iexact=name)
    except:
        return render(request, 'detail.html',{'error':'No Data'})
    return render(request, 'detail.html',{'article':article,'count':count,'comment':comment,'sidebar':sidebar})

def category(request,name):
    error=""
    if name=='search':
        try:
            search=request.POST['search']
            content=Article.objects.filter(title__icontains=search)
        except:
            error='Error'
        if content.count()==0:
            error="No Data"

    else:
        content = Article.objects.filter(category__iexact=name).order_by('title')



    title=str.capitalize(name)
    recent=Article.objects.all().order_by('-date')[:10]
    sidebar = Article.objects.all().order_by('?')[:3]
    return render(request,'category.html',{'category':content,'title':title,'recent':recent,'sidebar':sidebar,'error':error})


def upload(request):
    if request.method == 'POST':
        username=request.user
        title=request.POST['name']
        age=request.POST['age']
        nationality=request.POST['nationality']
        thumbnail=request.FILES['thumbnail']
        banner=request.FILES['banner']
        category=request.POST['category']
        content=request.POST['content']
        Article.objects.create(author=User.objects.get(username=username),category=category,title=title,age=age,nationality=nationality,thumbnail=thumbnail,banner=banner,content=content)
        return HttpResponseRedirect('detail-'+title)
    username=request.user
    comment=Comment.objects.filter(user__user__username=username)
    return render(request,'upload.html',{'comment':comment})

