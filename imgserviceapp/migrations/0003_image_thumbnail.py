# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgserviceapp', '0002_image_commentamount'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='thumbnail',
            field=models.ImageField(upload_to='images/thumbnails', default=''),
            preserve_default=False,
        ),
    ]
