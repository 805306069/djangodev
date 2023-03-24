from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection

# Create your views here.
from django.views import View

from app02.models import UserInfo2, Department2


def index(request):
    """生成数据的俩种方式"""
    # 方式一：
    # obj = UserInfo2(ids=7, name='菜蔬', password='mysql608420-', age=33, user_id='IT008326')
    # obj.save()
    # 方式二：
    # UserInfo2.objects.create(ids=9, name='玉昆', password='mysql608420-', age=24, user_id='IT008446')
    userinfo_2 = UserInfo2.objects.filter(age__gt=24)
    Department2.objects.create(title_liter="leige", UserInfo_id=userinfo_2.first().ids)
    return HttpResponse("我的app02页面")

class read_userinfo(View):

    def get(self, request):#, age
        """读取数据"""
        #方式一：读取多条数据
        userinfo = UserInfo2.objects.all()

        # 方式二：读取单条数据
        # userinfo_1 = UserInfo2.objects.get(age=age)
        # userinfo_2 = UserInfo2.objects.filter(age__gt=24)
        userinfo_3 = UserInfo2.objects.get(ids=4).ids
        print(Department2.objects.get(UserInfo_id=userinfo_3).id)
        userinfo_4 = Department2.objects.filter(UserInfo__user_id='IT008106').update()

        return HttpResponse("读取数据成功")



