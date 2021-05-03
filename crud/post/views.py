from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

# Add method
def add(request):
    return render(request, 'add.html')

# Update method
def update(request, id):
    return render(request, 'update.html')