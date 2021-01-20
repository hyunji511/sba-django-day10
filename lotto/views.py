from django.shortcuts import render
from django.http.response import HttpResponse
import random

# Create your views here.
def index(req):
    req.GET.get('num','')
    if req.method == 'GET' :
        lotto = []
        while len(lotto) < 6:
            lotto.append(random.randint(1,46))
            lotto = list(set(lotto))
            #set으로 중복제거
            #print(lotto)
            return HttpResponse(f"<h1>lotto 번호 추첨 { lotto }</h1>")
    return HttpResponse("post")