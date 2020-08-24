from django.conf.urls import url,include
from django.contrib import admin
from page import views as page_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$',page_views.index,name='index'),
    url(r'^page/',include('page.urls')),
    url(r'^articles/',include('articles.urls')),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^contact/',include('contacts.urls')),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
