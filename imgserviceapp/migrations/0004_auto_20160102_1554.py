# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgserviceapp', '0003_image_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='description',
            field=models.CharField(max_length=4000, default=''),
        ),
        migrations.AlterField(
            model_name='image',
            name='thumbnail',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
