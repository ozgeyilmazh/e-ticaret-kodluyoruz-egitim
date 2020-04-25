from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils.text import slugify
from .models import Carousel, Page
from .forms import CarouselModelForm, PageModelForm
from django.contrib.admin.views.decorators import staff_member_required
from product.models import Category, Product

STATUS = "published"

def index(request):
    context = dict()
    context['images'] = Carousel.objects.filter(status=STATUS).exclude(cover_image='')
    # context['categories'] = Category.objects.filter(status=STATUS).order_by('title')
    products = Product.objects.filter(is_home=True, status=STATUS,)
    context['products'] = products
    # if not request.session.session_key:
    #    request.session.save()
    # print(f"Session key: {request.session.session_key}")
    return render(request, 'home/index.html', context)

def page_show(request, slug):
    context = dict()
    context['page'] = get_object_or_404(Page, slug=slug)
    return render(request, 'page/page.html', context)

def manage_list(request):
    context = dict()
    return render(request, 'manage/manage.html', context)

@staff_member_required
def page_list(request):
    context = dict()
    context['items'] = Page.objects.all().order_by('-pk')
    return render(request, 'manage/page_list.html', context)

def page_create(request):
    context = dict()
    context['title'] = "Page Create Form"
    context['form'] = PageModelForm()

    if request.method == 'POST':
        form = PageModelForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.slug = slugify(item.title.replace('ı','i'))
            item.save()
            messages.success(request, 'Birseyler eklendi')
    return render(request, 'manage/form.html', context)

def page_update(request, pk):
    context = dict()
    item = Page.objects.get(pk=pk)
    context['title'] = f"{ item.title } - { item.pk } Page Create Form"
    context['form'] = PageModelForm(instance=item)
    if request.method == 'POST':
        form = PageModelForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            if item.slug == "":
                item.slug = slugify(item.title.replace('ı','i'))
            item.save()
            messages.success(request, 'guncellendi ;)')
            return redirect('page_update', pk)
    return render(request, 'manage/form.html', context)

def page_delete(request, pk):
    item = Page.objects.get(pk=pk)
    item.status= "deleted"
    item.save()
    return redirect('page_list')

def carousel_list(request):
    context = dict()
    context['carousel'] = Carousel.objects.all().order_by('-pk')
    return render(request, 'manage/carousel_list.html', context)
    
def carousel_update(request, pk):
    context = dict()
    item = Carousel.objects.get(pk=pk)
    context['title'] = f"{ item.title } - { item.pk } Carousel Create Form"
    context['form'] = CarouselModelForm(instance=item)
    if request.method == 'POST':
        form = CarouselModelForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'guncellendi ;)')
            return redirect('carousel_update', pk)
    return render(request, 'manage/form.html', context)
    
def carousel_create(request):
    context = dict()
    context['form'] = CarouselModelForm()
    context['title'] = "Carousel Create Form"
    if request.method == 'POST':
        form = CarouselModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Birseyler eklendi ama ne oldu bilemiyorum')
    return render(request, 'manage/form.html', context)