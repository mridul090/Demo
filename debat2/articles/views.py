from django.shortcuts import render,redirect
from django.http import HttpResponse
from articles.models import Article,Comment
from .import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
def articles_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request,'articles/article_list.html',context={'articles':articles})

#def article_details(request,id):
#    #return HttpResponse(slug)
#    article = Article.objects.get(id=id)
#    return render(request,'articles/article_details.html',context={'article':article})
def all_list_view(request):
    articles = Article.objects.all().order_by('date')
    return render(request,'articles/all_blog_list.html',context={'articles':articles})


def article_details(request,id):
    #return HttpResponse(id)
    if request.method == "POST":
        message = request.POST.get('message')
        user_name = request.POST.get('user_name')
        post_id = id
        Comment.objects.create(message = message,user_name  = user_name,post_id_id=int(id))
    article = Article.objects.get(id=id)
    comment = Comment.objects.all().filter(post_id=id)
    return render(request,'articles/article_details.html',context={'article':article,'comment':comment} )

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == "POST":
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid:
            #save in database
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect("articles:list")
    else:
        form = forms.CreateArticle()
    return render(request,'articles/article_create.html',context={'form':form})
