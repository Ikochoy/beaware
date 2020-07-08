from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    liked_post = models.CharField(max_length=100000, default="")
    disliked_posts = models.CharField(max_length=100000, default="")
    liked_comments = models.CharField(max_length=100000, default="")
    dislike_comments = models.CharField(max_length=100000, default="")


class Post(models.Model):
    title = models.CharField(max_length=1000)
    content = models.CharField(max_length=100000000)
    category = models.CharField(max_length=1000)
    release_date = models.DateField()
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)


class Comment(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=100000)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    reply = models.BooleanField(default=False)
    reply_comment_id = models.IntegerField(null=True, blank=True)

    def get_reply_comment(self):
        return Comment.objects.get(pk=self.reply_comment_id)

    def get_reply_username(self):
        return self.get_reply_comment().user.user.username
