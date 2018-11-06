from django.db import models

# Create your models here.


class HouseInfo(models.Model):
    title = models.CharField(max_length=256, verbose_name='标题')
    house = models.CharField(max_length=20, verbose_name='小区')
    bedroom = models.CharField(max_length=20, verbose_name='房厅')
    area = models.CharField(max_length=20, verbose_name='面积')
    direction = models.CharField(max_length=20, verbose_name='朝向')
    floor = models.CharField(max_length=60, verbose_name='朝向')
    year = models.CharField(max_length=10, verbose_name='年份')
    location = models.CharField(max_length=10, verbose_name='位置')
    total_price = models.IntegerField(verbose_name='总结(万元)')
    unit_price = models.IntegerField(verbose_name='单价(元/平方米)')

    add_date = models.DateTimeField(auto_now_add=True, verbose_name="创建日期")
    mod_date = models.DateTimeField(auto_now=True, verbose_name="修改日期")

    def __str__(self):
        return "{}-{}-{}".format(self.house,self.bedroom, self.total_price)

    class Meta:
        verbose_name = "二手房"



