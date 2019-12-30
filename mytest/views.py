from django.shortcuts import render

def post_list(request):
	return render(request, 'mytest/blog_list.html', {})
