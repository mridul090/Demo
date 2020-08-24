from django.conf.urls import url
from .import views

app_name='articles'

urlpatterns = [
    url(r"^list/",views.articles_list,name='list'),
    url(r'^create/$',views.article_create,name='create'),
    url(r'^AllList/$',views.all_list_view,name='all_list'),
    url(r'^(?P<id>[\w-]+)/$',views.article_details,name='details'),

]
