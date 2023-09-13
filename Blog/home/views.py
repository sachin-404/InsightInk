from django.shortcuts import render, redirect
from . import form
from . import models

# Create your views here.

def home(request):
    context = {'blogs': models.BlogModel.objects.all()}
    return render(request, 'home.html', context)

def login_view(request):
    return render(request, 'login.html')

def blog_detail(request, slug):
    context = {}
    try:
        blog_obj = models.BlogModel.objects.filter(slug = slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'blog_detail.html', context)

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

def signup_view(request):
    return render(request, 'signup.html')