from django.db import models
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

class Image(models.Model):
    title = models.CharField(max_length=50, default = '')
    photographer = models.CharField(max_length=30, default = '')
    description = models.CharField(max_length=4000, default = '')
    img = models.ImageField(upload_to = 'images/')
    createtime = models.DateTimeField(auto_now_add = True)
    commentAmount = models.IntegerField(default = 0)
    thumbnail = models.ImageField(upload_to='images/')

    def create_thumbnail(self):

             from PIL import Image
             from io import BytesIO
             from django.core.files.uploadedfile import SimpleUploadedFile
             import os

             # Set our max thumbnail size (max width, max height)
             THUMBNAIL_SIZE = (245,245)

             DJANGO_TYPE = self.img.file.content_type

             if DJANGO_TYPE == 'image/jpeg':
                 PIL_TYPE = 'jpeg'
                 FILE_EXTENSION = 'jpg'
             elif DJANGO_TYPE == 'image/png':
                 PIL_TYPE = 'png'
                 FILE_EXTENSION = 'png'

             # Open original photo which we want to thumbnail using PIL's Image
             image = Image.open(BytesIO(self.img.read()))

             # We use our PIL Image object to create the thumbnail, which already
             # has a thumbnail() convenience method that contrains proportions.
             # Additionally, we use Image.ANTIALIAS to make the image look better.
             # Without antialiasing the image pattern artifacts may result.
             image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

             # Save the thumbnail
             temp_handle = BytesIO()
             image.save(temp_handle, PIL_TYPE)
             temp_handle.seek(0)

             # Save image to a SimpleUploadedFile which can be saved into
             # ImageField
             suf = SimpleUploadedFile(os.path.split(self.img.name)[-1],
                     temp_handle.read(), content_type=DJANGO_TYPE)
             # Save SimpleUploadedFile into image field
             self.thumbnail.save('%s_thumbnail.%s'%(os.path.splitext(suf.name)[0],FILE_EXTENSION), suf, save=False)


class Comment(models.Model):
    name = models.CharField(max_length = 30, default = '')
    text = models.CharField(max_length = 1000, default = '')
    createTime = models.DateTimeField(auto_now_add = True)
    image = models.ForeignKey(Image, related_name = "comments")
