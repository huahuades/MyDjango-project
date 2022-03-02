from django.db import models
# Create your models here.

class Usermessage(models.Model):
    username=models.CharField('用户姓名',max_length=30,default='',unique=True)
    password=models.CharField('用户密码',max_length=32)
    telephone=models.IntegerField('用户电话号码',null=True)
    created_time=models.DateTimeField('创建时间',auto_now_add=True)
    updated_time=models.DateTimeField('更新时间',auto_now=True)
    class Meta:
        db_table='Usermessage'
        verbose_name='用户信息'
        verbose_name_plural=verbose_name

def __str__(self):
    return '%s'%(self.username)