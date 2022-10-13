# Generated by Django 3.2.5 on 2022-08-30 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20220828_0241'),
    ]

    operations = [
        migrations.CreateModel(
            name='articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_class', models.SmallIntegerField(choices=[(1, '论文'), (2, '精品论文'), (3, '专利'), (4, '奖项'), (5, '其他')], null=True, verbose_name='类型')),
                ('name', models.CharField(max_length=256, null=True, verbose_name='文献标题')),
                ('abstract', models.TextField(max_length=1024, null=True, verbose_name='摘要(50个单词以内)')),
                ('autor', models.CharField(max_length=256, null=True, verbose_name='作者')),
                ('journal', models.CharField(max_length=64, null=True, verbose_name='期刊')),
                ('birthday', models.DateTimeField(default='2022-9', null=True, verbose_name='发布时间')),
                ('href', models.CharField(max_length=1024, null=True, verbose_name='文献链接')),
            ],
        ),
        migrations.AlterField(
            model_name='members',
            name='create_time',
            field=models.IntegerField(default=2022, null=True, verbose_name='入学年份'),
        ),
    ]
