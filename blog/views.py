from django.template import loader, Context
from django.http import HttpResponse
from blog.models import BlogPost, Book
from django.db.models import Q
# Create your views here.
def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template("archive.html")
    c = {"posts": posts}

    book = Book.objects.get(title="张三的书")
    Book.objects.all().order_by("title", "last")
    Book.objects.all().distinct("title")
    # Book.objects.filter(last="Doe").exclude(Q(first="John") | Q(middle="Quincy"))
    Book.objects.all().extra()
    authors = book.authors.all()
    books = authors[1].book_set.all()
    print(books)

    a = Book.objects.filter(authors__name__endswith="四",
                            authoring__collaboration_type__contains="1")
    print(a)
    return HttpResponse(t.render(c))
