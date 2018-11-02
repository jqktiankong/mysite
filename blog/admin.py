from django.contrib import admin
from blog.models import BlogPost, Author, Book, Authoring
# Register your models here.
admin.site.register([BlogPost, Author, Book, Authoring])