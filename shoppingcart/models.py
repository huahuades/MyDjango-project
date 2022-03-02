from django.db import models
from users.models import Usermessage

# Create your models here.
class Cart(models.Model):
    shopname=models.CharField('物品名称',max_length=50,default='')
    shopsize=models.CharField('物品大小',max_length=20,default='')
    shopprice=models.DecimalField('物品价钱',max_digits=7,decimal_places=2,default='',null=True)
    shopquantity=models.IntegerField('物品余量',null=True)
    usermessage=models.ForeignKey(Usermessage,on_delete=models.CASCADE)
    is_active=models.BooleanField('是否活跃',default=True)
    class Meta:
        db_table='Cart'
        verbose_name='购物车'
        verbose_name_plural=verbose_name

    def __str__(self):
        return '%s'%(self.shopname)

