import random
import datetime
from django.shortcuts import render
# Create your views here.

# 2. 요청을 처리할 함수 정의
def index(request):
    # 2. >> 로직 작성 <<
    # 3. 해당하는 템플릿 반환
    return render(request, 'pages/index.html')

def hello(request, name):
    context = {'name':name}
    return render(request, 'pages/hello.html', context)

def lotto(request):
    print(request)
    print(type(request))
    # print(request.META)
    # 로직
    lotto_num = sorted(random.sample(range(1,46),6))
    # 변수를 딕셔너리에 담아서(보통 context라고 부름)
    context = {'lotto_num' : lotto_num}
    # render 할때 3번째 인자로 넘겨준다.
    # render 함수의 필수 인자 : request, template 파일
    # 변수를 넘겨주고 싶으면 3번째 인자로 dictionary를 넘겨준다.
    # Django에서 활용하는 템플릿 언어는 Django Template Language(DTL)
    return render(request, ' pages/lotto.html', context)

def dinner(request):
    menus = ['롯데리아', '편도', '맘스터치', '응급실떡볶이', '노은각', '파파존스', '후참집']
    pick = random.choice(menus)
    context = {
        'pick' : pick,
        'menus' : menus,
        'users' : [],
        'sentence' : 'Life is short, You need Python + django !',
        'datetime_now' : datetime.datetime.now(),
        'google_link' : 'http://www.google.com',
    }
    return render(request, 'pages/dinner.html', context)

def cube(request, num):
    context= { 
        'num' : num**3,
        'numbers' : [1, 2, 3, 4, 5],
        'student' : {
            '지수' : '지수!',
            '태수' : '태수!' 
        }
    }
    return render(request, 'pages/cube.html', context)

def about(request, name, age):
    context= {
        'name': name,
        'age' : age
    }
    return render(request, 'pages/about.html', context)

def isitgwangbok(request):
    today = datetime.datetime.now()
    D = today.strftime('%m %d')
    what = 0
    if D == '08 15':
        what = '네'
    else:
        what = '아니요'
    context = {
        'what' : what
    }
    return render(request, 'pages/isitgwangbok.html', context)

def ping(request):
    return render(request, 'pages/ping.html')

def pong(request):
    # 사용자가 넘겨주는 값 받아오기
    print(request.GET)
    # QueryDict {'data' : '안녕하세요'}
    data = request.GET.get('data')
    context = {
        'data' : data
    }
    return render(request, 'pages/pong.html', context)

def signup(request):
    return render(request, 'pages/signup.html')

def signup_result(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    password_confirmation = request.POST.get('password_confirmation')
    flag = False

    if password == password_confirmation:
        flag = True

    context = {
        'username' : username,
        'password' : password,
        'password_confirmation' : password_confirmation,
        'flag' : flag,
    }
    return render(request, 'pages/signup_result.html', context)
    