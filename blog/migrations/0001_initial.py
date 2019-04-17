# Generated by Django 2.1 on 2019-04-16 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(max_length=100, verbose_name='标题')),
                ('brief_content', models.TextField(verbose_name='摘要')),
                ('content', models.TextField(verbose_name='内容')),
                ('publish_date', models.DateTimeField(auto_now=True, verbose_name='发布时间')),
                ('article_click', models.IntegerField(default=0, verbose_name='浏览量')),
                ('article_dianzan', models.IntegerField(default=0, verbose_name='点赞数')),
                ('article_key', models.CharField(max_length=30, verbose_name='标签(栏目)')),
            ],
        ),
    ]
