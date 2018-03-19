from django.shortcuts import render

from main.models import Article
from comments.models import Comment

from django.http import HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse


def article_view(request, art_id):
    article = Article.objects.get(id=art_id)
    comment = Comment.objects.filter(article_id = art_id)
    print(comment)
    context = {
        'article': article,
        'comment': comment
    }
    return render(request, 'main/single_article.html', context)
def main_view(request):
    articles = Article.objects.all()[:10]
    context = {
        "articles": articles,
    }
    return render(request, 'main/home.html', context)

def add_article(request):
    if request.user.is_authenticated and request.POST:
        print(request.POST)
        article = Article()
        article.author= request.user
        article.title = request.POST["article_title"]
        article.content = request.POST["article_body"]
        article.save()
        return redirect(request.META['HTTP_REFERER'])
    else:
        return render(request, 'main/add-article.html')
