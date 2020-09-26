from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
	title = models.CharField(max_length = 200)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def published(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Блог'
		verbose_name_plural = 'Блоги'

class Author(models.Model):
	post = models.ForeignKey(Post, on_delete = models.CASCADE)
	f_name = models.CharField(max_length=100, verbose_name='Name')
	l_name = models.CharField(max_length=150, verbose_name='Last Name')

	def __str__(self):
		return self.l_name

	