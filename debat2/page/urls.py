from django.conf.urls import url
from page import views

app_name = 'page'

urlpatterns = [
    url(r'^about/',views.about,name='about'),
    url(r'^contuct/',views.contuct,name='contuct'),
]
