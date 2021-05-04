from django.shortcuts import render
from .models import Post
from django.contrib import messages

def home(request):
    posts=Post.objects.all()
    return render(request, 'home.html',{'posts':posts})

# Add method
def add(request):
    if request.method=='POST':
        title=request.POST['title']
        detail=request.POST['detail']
        Post.objects.create(title=title,detail=detail)
        messages.success(request, 'Data has been added')
    return render(request, 'add.html')

# Update method
def update(request, id):
    return render(request, 'update.html')