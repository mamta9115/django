from django.shortcuts import render
from .models import Contact
# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')
def about(request):
    return render(request, 'myapp/about.html')
def contact(request):
    if request.method == 'POST':
        n = request.POST['name']
        e = request.POST['email']
        m = request.POST['message']
        t = Contact(name=n, email=e, message=m)
        t.save()
    return render(request,  'myapp/contact.html')
