from django.shortcuts import render, HttpResponse, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import CreateArticle


def article_list(request):
    # names = []
    # for i in range(3):
    #     # name = input("please enter ur name: ")
    #     # names.append(name)
    # # names = ["Alex", "Omry"]

    articles = Article.objects.all().order_by('date')
    return render(request, "articles/article_list.html", {"articles": articles})


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    articles = Article.objects.all().order_by('date')
    return render(request, "articles/article_detail.html", {"article": article, "articles":articles})


@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == "POST":
        form = CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect("articles:list")
    else:
        form = CreateArticle()
    return render(request, "articles/article_create.html", {"form":form})