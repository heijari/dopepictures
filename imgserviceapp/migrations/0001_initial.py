# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=30, default='')),
                ('text', models.CharField(max_length=1000, default='')),
                ('createTime', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=50, default='')),
                ('photographer', models.CharField(max_length=30, default='')),
                ('description', models.TextField(default='')),
                ('img', models.ImageField(upload_to='images/')),
                ('createtime', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.ForeignKey(related_name='comments', to='imgserviceapp.Image'),
        ),
    ]
