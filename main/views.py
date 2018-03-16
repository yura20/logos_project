from django.shortcuts import render

from main.models import Article
from comments.models import Comment


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
