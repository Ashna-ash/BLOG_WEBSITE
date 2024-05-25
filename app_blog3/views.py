from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from.models import BlogPost,Comment
from .forms import BlogPostForm,CommentForm
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate,login,logout
from .models import MyBlog


def home(request):
    return render(request, 'base.html')
def Register(request):

        if request.method == 'POST':
            username = request.POST.get("username")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')

            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "user name already taken")
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, "email already taken")
                    return redirect('register')

                else:
                    user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                    email=email, password=password1)
                    user.save()
                    print("user created")
                    messages.info(request, "User created successfully")
                    return redirect('/')

            else:
                print("password not matching")
                messages.info(request, "password not matching")
                return redirect('register')
        else:
            return render(request,'register.html')


def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
        else:
            messages.error(request, "Invalid Credentials")
        return render(request, 'register.html')
    return render(request, "login.html")

def add_blogs(request):
    if request.method=="POST":
        form = BlogPostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.save()
            obj = form.instance
            alert = True
            return render(request, "base.html",{'obj':obj, 'alert':alert})
    else:
        form=BlogPostForm()
    return render(request, "add_blogs.html", {'form':form})


def blogs(request):
        posts = BlogPost.objects.all().order_by('-dateTime')
        return render(request, "blog.html", {'posts': posts})
def view_blog(request, desc):
    post = get_object_or_404(BlogPost, desc=desc)
    comments = post.comments.all()
    form = CommentForm()

    return render(request, 'view_blog.html', {'post': post, 'comments': comments, 'form': form})


def add_comment(request, desc):
    post = get_object_or_404(BlogPost, desc=desc)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.blog = post
            comment.save()
            return redirect('view_blog', desc=post.desc)

    return redirect('home')  # Redirect to home if the form submission fails

def user_logout(request):
    logout(request)

    return redirect('home')


def delete_blog(request, desc):
    # Retrieve the blog post with the given description
    post = get_object_or_404(BlogPost, desc=desc)

    # Check if the logged-in user is the author of the blog post
    if request.user == post.author:
        post.delete()
        return redirect('blogs')
    else:
        messages.error(request, "You are not allowed to delete this post.")
        return redirect('blogs')

def my_blogs(request):
    if not request.user.is_authenticated:
        return redirect('login')

    # Retrieve blogs created by the current user
    blogs = BlogPost.objects.filter(author=request.user)

    context = {
        'blogs': blogs
    }
    return render(request, 'myblogs.html', context)
