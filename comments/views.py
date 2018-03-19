from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.shortcuts import redirect
from comments.models import Comment
from django.urls import reverse
# Create your views here.

def add_comment(request, article_id):
    if request.user.is_authenticated and request.POST:
        print(request.POST)
        comment = Comment()
        comment.author= request.user
        comment.article_id = article_id
        comment.content = request.POST["comment_body"]
        comment.save()
        return redirect(
            reverse("main:single_art", args=[article_id])
        )
    else:
        return HttpResponseNotFound()
