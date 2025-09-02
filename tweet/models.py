from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    photo = models.ImageField(upload_to='photo/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_tweets', blank=True)
    retweets = models.ManyToManyField(User, related_name='retweeted_tweets', blank=True)
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'
    
    def total_likes(self):
        return self.likes.count()
    
    def total_retweets(self):
        return self.retweets.count()
    
    def total_replies(self):
        return self.replies.count()

class Twiit(models.Model):
    text = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]