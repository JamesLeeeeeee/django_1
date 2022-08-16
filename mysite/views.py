# 뷰: 기능을 담당(페이지 단위)
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    html = f"<html><h><a href='http://127.0.0.1:8000/welcome'> Welcome </a></h1></html>"
    return HttpResponse(html)


def welcome(request):
    html = "<html>Welcome</html>"
    return HttpResponse(html)


def template_test(request):
    # 기본 템플릿 폴더
    # 1. admin 앱
    # 2. 각 앱의 폴더에 있는 templates 폴더
    # 3. 설정한 폴더

    return render(request, 'test.html')
