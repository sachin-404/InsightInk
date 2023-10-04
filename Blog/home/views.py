from django.shortcuts import render, redirect
from django.contrib.auth import logout
from . import form
from . import models

# Create your views here.

def home(request):
    context = {'blogs': models.BlogModel.objects.all(),
               'latest': models.BlogModel.objects.first()}
    # latest = {'latest': models.BlogModel.objects.first()}
    # print(latest)
    
    return render(request, 'home.html', context)

def login_view(request):
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def blog_detail(request, slug):
    context = {}
    try:
        blog_obj = models.BlogModel.objects.filter(slug = slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'blog_detail.html', context)

def see_blog(request):
    context = {}
    try:
        blog_objs = models.BlogModel.objects.filter(user = request.user)
        context['blog_objs'] = blog_objs
    except Exception as e:
        print(e)
    return render(request, 'see_blog.html', context)

def add_blog(request):
    context = {'form': form.BlogForm}
    try:
        if request.method == 'POST':
            form_data = form.BlogForm(request.POST)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user
            
            if form_data.is_valid():
                content = form_data.cleaned_data['content']
            
            models.BlogModel.objects.create(
                user=user,
                title=title,
                content=content,
                image=image
            )
            return redirect('/add-blog')
            
    except Exception as e:
        print(e)
        
    return render(request, 'add_blog.html', context)

def delete_blog(request, id):
    try:
        blog_obj = models.BlogModel.objects.get(id= id)
        if blog_obj.user == request.user:
            blog_obj.delete()
    except Exception as e:
        print(e)
    return redirect('/see-blog')

def update_blog(request, slug):
    context = {}
    try:
        blog_obj = models.BlogModel.objects.get(slug = slug)
        
        if blog_obj.user != request.user:
            return redirect('/')
        
        initial_dict = {'content': blog_obj.content}
        blog_form = form.BlogForm(initial=initial_dict)
        
        if request.method == 'POST':
            form_data = form.BlogForm(request.POST)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user
            
            if form_data.is_valid():
                content = form_data.cleaned_data['content']
            
            models.BlogModel.objects.create(
                user=user,
                title=title,
                content=content,
                image=image
            )
        
        context['blog_obj'] = blog_obj
        context['form'] = blog_form
    except Exception as e:
        print(e)
    return render(request, 'update_blog.html', context)

def signup_view(request):
    return render(request, 'signup.html')