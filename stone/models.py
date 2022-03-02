from django.db import models

# Create your models here.
class Stone(models.Model):
    name=models.CharField('砖名',max_length=50,default='青砖')
    size=models.CharField('尺寸',max_length=20,default='')
    price=models.DecimalField('价钱',max_digits=7,decimal_places=2) 
    quantity=models.IntegerField('余量')
    class Meta:
        db_table='stone'
        verbose_name='石头类'
        verbose_name_plural=verbose_name
    def __str__(self):
        return '%s'%(self.name)