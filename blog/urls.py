"""blog URL Configuration"""


from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.views.static import serve
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='posts/')),
    url(r'posts/', include('posts.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_route': MEDIA_ROOT}),
]
