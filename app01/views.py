from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app01.models import Department, UserInfo


def index(request):
    return HttpResponse("我的第一个views页面")


def user_list(request):
    return render(request, "user_list.html")


def news(request):
    # import requests
    return render(request, "news.html")


def something(request):
    print(request.method)
    print(request.GET)
    return HttpResponse("request请求方法")


def orm(request):
    # Department.objects.create(title_liter="销售")
    # Department.objects.create(title_liter="开发")
    # Department.objects.create(title_liter="测试")
    Department.objects.filter(id=3).delete()
    UserInfo.objects.create(name="陈赫", age=29, password="mysql608420-", user_id="root")
    return HttpResponse("创建成功")

def getsql(request):
    UserInfo.objects.filter(id=3).update(age=28, name="蔡卓")
    selinfo = UserInfo.objects.all()
    for obj in selinfo:
        print(obj.age, obj.name, obj.user_id)
    UserInfo.objects.filter(id=2).update(age=26,name="弹布尔")
    return HttpResponse(selinfo.first())
