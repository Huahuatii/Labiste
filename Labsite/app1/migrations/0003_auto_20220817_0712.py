# Generated by Django 3.2.5 on 2022-08-17 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_members_create_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='members',
            name='Codename',
        ),
        migrations.AlterField(
            model_name='members',
            name='age',
            field=models.IntegerField(default=18, null=True, verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='members',
            name='description',
            field=models.CharField(default='货拉拉拉不拉拉布拉多', max_length=256, null=True, verbose_name='个人描述'),
        ),
        migrations.AlterField(
            model_name='members',
            name='email',
            field=models.CharField(default='caiji88@zju.edu.cn', max_length=64, null=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='members',
            name='native_place',
            field=models.CharField(default='浙江杭州', max_length=64, null=True, verbose_name='籍贯'),
        ),
    ]
