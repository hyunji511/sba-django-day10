from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Members

# Create your views here.
def login(req):
    if req.method == 'GET' :
        return render(req, 'login.html')
    elif req.method =='POST' :
        useremail= req.POST.get('username',None)
        email = req.POST.get('useremail',None)

        err = {}
        #딕셔너리 파일로 받음 : key와 value로

        if not(useremail and username) :
            err['err'] = '유효성이 잘못되었습니다.'
            return render(req, 'login.html')

def gu(req):
    num = req.GET.get('num','')
    return HttpResponse(f"<h1> gugu :{num_gugu(num)} </h1>")

def num_gugu(num) :
    str =""
    for i in range(9):
        str += f"{int(num)}*{i+1}={int(num)*(i+1)} <br>"
    return str

def index(req):
    print(dir(req))
    return HttpResponse("<h1>version 1 : Hello World</h1>")

def git(req):
	return HttpResponse("<h2>git version</h2>")

def test(req):
    return HttpResponse("<h2>Test</h2>")

def signup(req):
    if req.method == 'POST' :
        username = req.POST['username']
        email = req.POST['email']

        member = Members(
            username = username,
            useremail = email
        )
       
        member.save()
        res_data = {}
        res_data['res'] = '등록성공'
        return render(req, 'index.html', res_data)

    return render(req, 'index.html') 



# Create your views here.
