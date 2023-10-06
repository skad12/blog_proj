from django.shortcuts import render

posts = [
    {
        'author': 'SKAD',
        'title': 'Daily Tech Tips and Tricks with SKAD',
        'content': 'First post content',
        'date_posted': 'September 16, 2023'
    },


]


def home(request):
    context = {
        'title': 'Home',
        'posts': posts,

    }
    return render(request, 'blog/home.html', context)


def contact(request):
    return render(request, 'blog/contact.html', {'title': 'contacts'})


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
