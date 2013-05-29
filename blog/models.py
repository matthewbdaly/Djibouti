from django.db import models
from django.contrib.auth.models import User
from markdown import markdown
from django.contrib.sites.models import Site


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40, unique=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/categories/%s/" % self.slug


class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    text = models.TextField()
    html_text = models.TextField(editable=False, blank=True, null=True)
    slug = models.SlugField(max_length=40, unique=True)
    author = models.ForeignKey(User)
    categories = models.ManyToManyField(Category, blank=True, null=True, through='CategoryToPost')
    site = models.ForeignKey(Site)

    class Meta:
        ordering = ["-pub_date"]


    def __unicode__(self):
        return self.title


    def get_absolute_url(self):
        return "/%s/%s/%s/" % (self.pub_date.year, self.pub_date.month, self.slug)


    def save(self):
        self.html_text = markdown(self.text, ['codehilite'])
        super(Post, self).save()


class CategoryToPost(models.Model):
    post = models.ForeignKey(Post)
    category = models.ForeignKey(Category)
