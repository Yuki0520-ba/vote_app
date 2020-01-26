from django.db import models

# Create your models here.
class Band(models.Model):
    band_name=models.CharField(verbose_name='バンド名',max_length=30)
    point=models.DecimalField(
        verbose_name='点数',
        default=0,
        max_digits=3, decimal_places=0
    )
    order=models.IntegerField(verbose_name='順番',default=0)
    posted_date=models.DateTimeField(auto_now_add=True)

    class Meta:
            ordering =['order','posted_date']
    
    def __str__(self): # adminサイトで作られるオブジェクトに可読性を持たせる
        return self.band_name


class Vote(models.Model):
    band = models.ForeignKey(Band,on_delete=models.CASCADE)
    count=models.IntegerField(default=0)

