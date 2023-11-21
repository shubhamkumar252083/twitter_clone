from django.db import models
from user.models import User

class Tweet(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    user_id = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, db_column="user_id")
    tweet = models.CharField(max_length=255, db_column="tweet")
    created_datetime = models.DateTimeField(auto_now_add=True, db_column="created_datetime")
    updated_at = models.DateTimeField(auto_now=True, db_column="updated_at")

    def __str__(self) -> str:
        return f'{self.id}'

    class Meta:
        db_table = 'tweet'


class CommentsAndStatus(models.Model):
    STATUS_CHOICES = (
    ('L', 'LIKE'),
    ('D', 'DISLIKE'),
    ('H', 'HEART'),
    ('N', 'NOTHING'),
    )
    id = models.AutoField(primary_key=True, db_column="id")
    user_id = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, db_column="user_id")
    comment = models.CharField(max_length=255, db_column="comment")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='N', db_column="status")
    tweet_id = models.ForeignKey(
        Tweet, on_delete=models.SET_NULL, null=True, blank=True, db_column="tweet_id")
    created_datetime = models.DateTimeField(auto_now_add=True, db_column="created_datetime")
    updated_at = models.DateTimeField(auto_now=True, db_column="updated_at")

    class Meta:
        db_table = 'comments_n_status'


class Hashtag(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    name = models.CharField(max_length=100, unique=True, db_column="name")
    tweets = models.ManyToManyField(Tweet, related_name='hashtags', db_column="tweets")
    created_datetime = models.DateTimeField(auto_now_add=True, db_column="created_datetime")
    updated_at = models.DateTimeField(auto_now=True, db_column="updated_at")

    class Meta:
        db_table = 'hashtag'











# test database


