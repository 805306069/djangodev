# Create your models here.
from app02.utils.base_model import BaseModel
from django.db import models


class UserInfo2(BaseModel):
    password = models.CharField(max_length=64, verbose_name="密码", help_text='help-pass')
    age = models.IntegerField()
    user_id = models.CharField(max_length=64,null=True,blank=True)
    basedate_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', null=True, blank=True)

    def __str__(self):
        return f"UserInfo2({self.name})"

class UserauthInfo2(BaseModel):
    user_id = models.CharField(max_length=64, null=True, blank=True)
    rolename = models.CharField(max_length=16, verbose_name='用户权限', help_text='用户权限')
    userDisplayName = models.TextField(max_length=32,verbose_name='最后修改人', help_text='最后修改人')


class Department2(models.Model):
    title_liter = models.CharField(max_length=16)
    UserInfo = models.ForeignKey('app02.UserInfo2', on_delete=models.CASCADE,
                                 verbose_name='所属用户', help_text='所属用户')

    class Meta:
        db_table = 'tb_app02depart'
