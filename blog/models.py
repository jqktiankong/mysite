from django.db import models
from django.contrib import admin


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

    class Mate:
        ordering = ("-timestamp",)


# class BlogPostAdmin(admin.ModelAdmin):
#     list_display = ("title", "timestamp")

# class Author(models.Model):
#     # 主键
#     name = models.CharField(max_length=100, primary_key=True)


# on_delete属性
# CASCADE:这就是默认的选项，级联删除，你无需显性指定它。
# PROTECT: 保护模式，如果采用该选项，删除的时候，会抛出ProtectedError错误。
# SET_NULL: 置空模式，删除的时候，外键字段被设置为空，前提就是blank=True, null=True,定义该字段的时候，允许为空。
# SET_DEFAULT: 置默认值，删除的时候，外键字段设置为默认值，所以定义外键的时候注意加上一个默认值。
# SET(): 自定义一个值，该值当然只能是对应的实体了
# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     # 外键 关联到Author表的name属性
#     author = models.ForeignKey(Author, to_field="name", related_name="books", on_delete=models.CASCADE)

# 多对多
class Author(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, through="Authoring")


class Authoring(models.Model):
    collaboration_type = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, to_field="name", on_delete=models.CASCADE)

class SmithBook(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, limit_choices_to={
        "name_endswith": "四"
    })