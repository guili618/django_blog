from django.db import models
from django.utils import timezone
#from django.core.urlresolvers import reverse
from django.urls import reverse
from django.contrib.auth.models import User

import django_tables2 as tables

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class PostTable(tables.Table):
    id = tables.Column()
    title = tables.Column()
    class Meta:
        model = Post
        attrs = {'class': 'ui selectable celled table'}
        template_name = 'django_tables2/semantic.html'




class Product(models.Model):
    name = models.CharField('名称',max_length=255)
    price = models.DecimalField('价格',max_digits=5, decimal_places=2)
    description = models.TextField('描述')
    release_date = models.DateField('发布日期')
    manufacturer = models.ForeignKey(User)