from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib import messages

from .forms import BlogForm, CommentForm
from .models import Blog, Comment

 

# Create your views here.
def post_create(request):
    blog_form = BlogForm()

    if request.method == 'POST':
        blog_form = BlogForm(request.POST or None, request.FILES or None)

        if blog_form.is_valid():
            # blog_form.save()
            profile = blog_form.save(commit=False)
            profile.user = request.user
            profile.save()

            
            messages.success(request, 'Post Created Succesfully!')
            return redirect('home')


    context = {
        'blog_form': blog_form
    }
    return render (request, 'blog/post_create.html', context)


def home(request):
    posts = Blog.objects.all()

    context = {
        'posts': posts
    }
    return render(request, 'users/home.html', context)

def post_update(request, id):
    blog = Blog.objects.get(id=id)
    blog_form = BlogForm(instance = blog)
    
    if request.method == "POST":
        blog_form = BlogForm(request.POST, instance = blog)
        if blog_form.is_valid():
            blog_form.save()
            return redirect('home')

    context = {
        'blog_form': blog_form
    }
    return render(request, 'blog/post-update.html', context)

def post_detail(request, id):
    blog = Blog.objects.get(id=id)
    user = Blog()
    comments_form = CommentForm()
    comment_shows = Comment.objects.all()

    if request.method == 'POST':
        comments_form = CommentForm(request.POST)

        if comments_form.is_valid():
            comments = comments_form.save(commit=False)
            comments.user = request.user
            comments.post = blog
            comments.save()
            
                        
            messages.success(request, 'Comment Created Succesfully!')
            return redirect('blog:detail')

    context = {
        'blog': blog,
        'user': user,
        'comments_form': comments_form,
        'comment_shows': comment_shows,
        
    }
    return render(request, 'blog/post-detail.html', context)


def post_delete(request, id):
    blog = Blog.objects.get(id=id)
    if request.method == "POST":
        blog.delete()
        return redirect("home")
    
    return render(request, 'blog/post-delete.html', { 'blog': blog })









