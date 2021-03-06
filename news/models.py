from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField(blank =True)
    phone_number = models.CharField(max_length=10,blank =True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['first_name']

    def save_editor(self):
        self.save()

    def delete_editor(self):
        self.delete()
    

class Tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def save_tags(self):
        self.save()

    def delete_tags(self):
        self.delete()

class Article(models.Model):
    title = models.CharField(max_length = 60)
    post = HTMLField()
    editor = models.ForeignKey(User,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'articles/', blank=True)

    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

    def save_article(self):
        self.save()

    def delete_article(self):
        self.delete()

    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news

    @classmethod
    def days_news(cls,date):
        news = cls.objects.filter(pud_date__date = date)
        return news    

    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news
        
class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()