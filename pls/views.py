from secrets import choice
from unittest import result
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
#from .forms import AnswerForm#,CheckForm
from pls.forms import LoginForm, UserCreateForm
from django.views import View
from .models import Answer, Kadai,Users,KadaiAdmin,KadaiQuestion,SelectInfo
from . import forms
from django.db.models import QuerySet

# Create your views here.

def log_in(req):
    return render(req, 'pls/log_in.html', {})

def home(req):
    return render(req, "pls/home.html", {})

def calender(request):
    data = KadaiAdmin.objects.all().filter(userid=request.user.id)#現在のユーザーIDとKadaiAdminのユーザーIDを照合
    kadai = Kadai.objects.all()
    request.session["user_id"] = request.user.id
    params = {
        'data':data,
        'userid':request.session["user_id"] ,
        'username':request.user.username,
        'kadai':kadai
    }    
    return render(request,'pls/calender.html',params)

class Create_account(CreateView):
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            #フォームから'username'を読み取る
            username = form.cleaned_data.get('username')
            #フォームから'password1'を読み取る
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/calender')
        return render(request, 'pls/register.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        return  render(request, 'pls/register.html', {'form': form,})

create_account = Create_account.as_view()

#ログイン機能
class Account_login(View):
    def post(self, request, *arg, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)#デフォルトUserテーブルからusernameを取り出す
            login(request, user)
            return redirect('/calender')
        return render(request, 'pls/login.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'pls/login.html', {'form': form,})

account_login = Account_login.as_view()

def Qdesc(request,kadai_id):
    question_cnt = Kadai.objects.all().values("question_cnt").get(kadai_id=kadai_id)#問題数
    params = {
        'kadai_id':kadai_id,
        'description':Kadai.objects.get(kadai_id=kadai_id),
        'question_cnt':question_cnt
    }
    return render(request,'pls/Qdesc.html',params)

def answer(request,kadai_id): 
    kadai_question = KadaiQuestion.objects.all().filter(kadai_id=kadai_id)
    kadai_question_item = SelectInfo.objects.all().filter(kadai_id=kadai_id)
    params = {
        'kadai_question':kadai_question,
        'kadai_question_item':kadai_question_item,
        'kadai_id':kadai_id
    }
    return render(request,'pls/answer.html',params)

def result(request,kadai_id):
    #question_cnt = KadaiQuestion.objects.all().filter(kadai_id=kadai_id).count()#問題数
    #question_cnt = Kadai.objects.all().values("question_cnt").get(kadai_id=kadai_id)
    #question_cnt = Kadai.objects.all().values("question_cnt").get(kadai_id=kadai_id)['question_cnt']
    question_cnt = Kadai.objects.all().values_list("question_cnt").get(kadai_id=kadai_id)[0]
    if request.method == 'POST':
        for x in range(question_cnt):
            QuestionAnswer = request.POST[str(x + 1)]
            UserId = Users(userid=request.user.id)
            KadaiId = Kadai(kadai_id=kadai_id)
            QuestionNum = KadaiQuestion(question_num=str(x + 1))
            answer =  Answer(
                userid=UserId,
                kadai_id=KadaiId,
                question_num=QuestionNum,
                question_answer=QuestionAnswer)
            answer.save()
    return render(request,"pls/result.html")