from main.models import Article
from comments.models import Comment
def latest_articles(request):
    articles = Article.objects.all().order_by("-created")[:3]
    articles_comments = Comment.objects.all().order_by("-id")[:5]
    return {
        "latest_articles": articles,
        "articles_comments": articles_comments
    }