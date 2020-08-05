from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
        Class representing posts.
    """

    title = models.CharField(max_length=128)
    link = models.URLField(max_length=128)
    creation_date = models.DateTimeField(auto_now_add=True)
    author_name = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def upvotes_count(self):
        """
            Total amount of upvotes of the post.
        """

        return Upvote.objects.filter(post=self).count()

    def add_upvote(self, user):
        """
            Adding an upvote to the post.
        """

        if Upvote.objects.filter(user__id=user.id).exists():
            return False
        Upvote.objects.create(user=user, post=self)
        return True


class Comment(models.Model):
    """
        Class representing comments.
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)


class Upvote(models.Model):
    """
        Class representing user's upvotes of the posts.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
