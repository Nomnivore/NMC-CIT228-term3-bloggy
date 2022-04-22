from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


class Blog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"@{self.user} - {self.name}"

    def published_set(self):
        return self.article_set.filter(published=True)

    def readable_article_count(self):
        return self.published_set().count()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    default_name = f"{instance.username}'s Blog"
    Blog.objects.get_or_create(
        user=instance, defaults={'name': default_name})


class Article(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()  # this will be markdown
    published = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def preview(self):
        return len(self.body) > 250 and self.body[:250] + '...' or self.body

    def __str__(self):
        return self.title
