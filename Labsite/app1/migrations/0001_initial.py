# Generated by Django 3.2.5 on 2022-08-11 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, null=True, verbose_name='姓名')),
                ('gender', models.SmallIntegerField(choices=[(1, '男'), (2, '女')], null=True, verbose_name='性别')),
                ('native_place', models.CharField(max_length=64, null=True, verbose_name='籍贯')),
                ('age', models.IntegerField(null=True, verbose_name='年龄')),
                ('Codename', models.CharField(max_length=16, null=True, verbose_name='代号')),
                ('description', models.CharField(max_length=256, null=True, verbose_name='个人描述')),
                ('birthday', models.DateTimeField(default='2022-9-1', null=True, verbose_name='生日')),
                ('email', models.CharField(max_length=64, null=True, verbose_name='邮箱')),
                ('QQ', models.CharField(max_length=16, null=True, verbose_name='QQ')),
                ('create_time', models.DateTimeField(default='2022', null=True, verbose_name='入学年份')),
                ('shortname', models.CharField(max_length=16, null=True, verbose_name='姓名缩写[例如: HHT]')),
            ],
        ),
    ]
