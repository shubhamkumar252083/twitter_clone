from django.db import models
from user.models import User

class Tweet(models.Model):
    id = models.AutoField(primary_key=True, db_column="fld_ai_id")
    user_id = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, db_column="fld_user_id")
    tweet = models.CharField(max_length=255, db_column="fld_tweet")
    created_datetime = models.DateTimeField(auto_now_add=True, db_column="fld_created_datetime")
    updated_at = models.DateTimeField(auto_now=True, db_column="fld_updated_at")

    def __str__(self) -> str:
        return f'{self.id}'

    class Meta:
        db_table = 'tbl_tweet'


class CommentsAndStatus(models.Model):
    STATUS_CHOICES = (
    ('L', 'LIKE'),
    ('D', 'DISLIKE'),
    ('H', 'HEART'),
    ('N', 'NOTHING'),
    )
    id = models.AutoField(primary_key=True, db_column="fld_ai_id")
    user_id = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, db_column="fld_user_id")
    comment = models.CharField(max_length=255, db_column="fld_comment")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='N', db_column="fld_status")
    tweet_id = models.ForeignKey(
        Tweet, on_delete=models.SET_NULL, null=True, blank=True, db_column="fld_tweet_id")
    created_datetime = models.DateTimeField(auto_now_add=True, db_column="fld_created_datetime")
    updated_at = models.DateTimeField(auto_now=True, db_column="fld_updated_at")

    class Meta:
        db_table = 'tbl_comments_n_status'


class Hashtag(models.Model):
    id = models.AutoField(primary_key=True, db_column="fld_ai_id")
    name = models.CharField(max_length=100, unique=True, db_column="fld_name")
    tweets = models.ManyToManyField(Tweet, related_name='hashtags', db_column="fld_tweets")
    created_datetime = models.DateTimeField(auto_now_add=True, db_column="fld_created_datetime")
    updated_at = models.DateTimeField(auto_now=True, db_column="fld_updated_at")

    class Meta:
        db_table = 'tbl_hashtag'











# test database


