from django.db import models


# Create your models here.
class Person(models.Model):
    """
    人物模型
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Person2(models.Model):
    """
    人物模型
    """
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)


class Musician(models.Model):
    """
    音乐家模型
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)


class Album(models.Model):
    """
    专辑模型
    """
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()


class Test(models.Model):
    """
    测试模型：测试help_text，失败，这个不能用
    """
    STATUS_LIST = (
        ('normal', '正常'),
        ('hidden', '隐藏'),
    )
    name = models.CharField(max_length=50, help_text='测试名称')
    status = models.CharField(max_length=20, choices=STATUS_LIST, help_text='测试状态,normal:正常，hidden:隐藏')


class Test2(models.Model):
    """
    依旧测试备注，失败，这个还是不是备注，是导出时用的表头
    """
    STATUS_LIST = (
        ('normal', '正常'),
        ('hidden', '隐藏'),
    )
    name = models.CharField(max_length=50, verbose_name='测试名称')
    status = models.CharField(max_length=20, choices=STATUS_LIST, verbose_name='测试状态,normal:正常，hidden:隐藏')


class Manufacturer(models.Model):
    pass


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)



