from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author' : 'Anirudh',
        'title' : 'Blog Post 1',
        'content' : 'The beast has arrived',
        'date_posted' : 'Nov 22 2020'
    },
    {
        'author' : 'Grishma',
        'title' : 'Blog Post 2',
        'content' : 'The real beast has arrived',
        'date_posted' : 'Nov 23 2020'
    }
]

def home(request):
    context = {
        'posts' : posts
    }

    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        'title' : 'About'
    }
    return render(request, 'blog/about.html', context)