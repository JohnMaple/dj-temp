# Generated by Django 2.1.3 on 2018-12-06 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0003_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='测试名称')),
                ('status', models.CharField(choices=[('normal', '正常'), ('hidden', '隐藏')], max_length=20, verbose_name='测试状态,normal:正常，hidden:隐藏')),
            ],
        ),
    ]
