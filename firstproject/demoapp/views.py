from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
    'author': 'Coreyms',
    'title':'blogpost1',
    'content':'first post content',
    'date_posted':'august 2,2022'
     },
     {
    'author': 'Coreyms',
    'title':'blogpost2',
    'content':'second post content',
    'date_posted':'august 3,2022'
     }
]

def home(request):
    context = {
        'posts':posts
     }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

