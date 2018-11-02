from blog.views import archive
from django.conf.urls import url

urlpatterns = [
    url(r"^$", archive)
]