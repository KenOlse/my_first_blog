from django.shortcuts import render
from .models import Post 

def post_list(request):
	urls = Post.objects.all()
	return render(request, 'mytest/blog_list.html', {'urls': urls})
