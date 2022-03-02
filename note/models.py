from django.db import models
from users.models import Usermessage
# Create your models here.
class Note(models.Model):
    title=models.CharField('标题',max_length=100)
    content=models.TextField('内容')
    created_time=models.DateTimeField('创建时间',auto_now_add=True)
    update_time=models.DateTimeField('更新时间',auto_now=True)
    usermessage=models.ForeignKey(Usermessage,on_delete=models.CASCADE)
    class Meta:
        db_table='note'
        verbose_name='意见反馈'
        verbose_name_plural=verbose_name

    def __str__(self):
        return '%s'%(self.title)