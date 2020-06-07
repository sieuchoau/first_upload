from django.shortcuts import render
from . import ML

def home(request):
    return render(request,'index.html')

def result(request):
    user_input = request.GET['user_input']
    user_input = ML.nhanlen(user_input)
    return render(request, 'result.html',{'home_input': user_input})
