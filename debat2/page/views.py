from django.shortcuts import render
from page.models import Slider,Content,OurTeam,ProgressBer,Testimonial
# Create your views here.

def index(request):
    slider = Slider.objects.order_by('photo_1')
    content = Content.objects.order_by('Title')
    ourteam = OurTeam.objects.order_by('Photo_1')
    progressbar = ProgressBer.objects.order_by('First')
    testimonial = Testimonial.objects.order_by('Details')
    return render(request,'debat/index.html',context={
    'slider':slider,
    'content':content,
    'ourteam':ourteam,
    'progressbar':progressbar,
    'testimonial':testimonial
    })

def about(request):
    content = Content.objects.order_by('Title')
    ourteam = OurTeam.objects.order_by('Photo_1')
    progressbar = ProgressBer.objects.order_by('First')
    return render(request,'debat/about.html',context={
    'content':content,
    'ourteam':ourteam,
    'progressbar':progressbar
    })

def contuct(request):
    return render(request,'debat/contuct.html')
