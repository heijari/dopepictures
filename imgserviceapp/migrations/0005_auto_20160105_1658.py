# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgserviceapp', '0004_auto_20160102_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='createTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='createtime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
