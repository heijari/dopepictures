from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload-new-picture$', views.add_new_photo, name='add_new_photo'),
    url(r'^gallery$', views.all_photos, name='all_photos'),
    url(r"^gallery/(?P<photo_id>[0-9]+)$", views.show_photo, name='show_photo')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
