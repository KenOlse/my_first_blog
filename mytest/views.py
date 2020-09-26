from django.shortcuts import render
from .models import Post, Author

def post_list(request):
	urls = Post.objects.all()
	context = {'urls': urls}
	return render(request, 'mytest/blog_list.html', context)

def entries(request, pk ):
	entry = Author.objects.get(pk=pk)
	context = {'entry': entry}
	return render(request, 'mytest/entry.html', context)
