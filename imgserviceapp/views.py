from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from imgserviceapp.models import Image,  Comment
from imgserviceapp.forms import CommentForm, ImageForm
from imgservice.settings import MEDIA_ROOT, MEDIA_URL

# Create your views here.
def index(request):
    return redirect(all_photos)


def add_new_photo(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = Image(title = form.cleaned_data['title'], photographer = form.cleaned_data['photographer'],
                    description = form.cleaned_data['description'], img = form.cleaned_data['img'])
            image.create_thumbnail()
            image.save()
            form = ImageForm()
            return redirect('all_photos')

    elif request.method == 'GET':
        form = ImageForm()
    return render(request, 'uploadform.html', {'form': form})


def show_photo(request, photo_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        # get stuff from the database
        img = Image.objects.get(pk=photo_id)
        comments = Comment.objects.filter(image=img).order_by('-pk')
        count = Comment.objects.filter(image=img).count()
        setattr(img, 'commentAmount', count)
        if form.is_valid():
            comment = Comment(name = form.cleaned_data['name'], text = form.cleaned_data['text'], image = img)
            comment.save()
            comments = Comment.objects.filter(image=img).order_by('-pk')
            form = CommentForm()
            return redirect('show_photo', photo_id=photo_id)
        else:
            form = CommentForm()
            return render(request, 'image.html', {'image': img, 'form': form, 'comments': comments })

    else:
        img = get_object_or_404(Image, pk=photo_id)
        count = Comment.objects.filter(image=img).count()
        setattr(img, 'commentAmount', count)
        form = CommentForm()
        comments = Comment.objects.filter(image=img).order_by('-pk')
        return render(request, 'image.html', {'image': img, 'form': form, 'comments': comments })


def all_photos(request):
    pics = Image.objects.all().order_by('-pk')
    for pic in pics:
        count = Comment.objects.filter(image=pic).count()
        setattr(pic, 'commentAmount', count)
    return render(request, 'gallery.html', {'images': pics, 'media_root': MEDIA_ROOT, 'media_url': MEDIA_URL})
