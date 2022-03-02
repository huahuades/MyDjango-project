from django.db import models

# Create your models here.
class Brick(models.Model):
    name=models.CharField('石头名称',max_length=50,default='道牙石')
    size=models.CharField('尺寸',max_length=20,default='')
    price=models.DecimalField('价钱',max_digits=7,decimal_places=2)
    quantity=models.IntegerField('余量')
    #这个is_active是用于伪删除的，将要伪删除的数据设置is_active为fasle
    is_active=models.BooleanField('是否活跃',default=True)
    class Meta:
        db_table='brick'
        verbose_name='砖类'
        verbose_name_plural=verbose_name

    def __str__(self):
        return '%s'%(self.name)