from django.db import models
from ckeditor.fields import RichTextField
from .IcoUtil import path_and_rename


# Create your models here.


class Contest(models.Model):
    title_in_english = models.CharField(max_length=200)
    title_in_persion = models.CharField(max_length=200)
    cover_in_english_image = models.ImageField(upload_to=path_and_rename)
    cover_in_persian_image = models.ImageField(upload_to=path_and_rename)

    def __str__(self):
        return self.title_in_english


class Gallery(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=path_and_rename)
    caption_in_english = models.CharField(max_length=500)
    caption_in_persian = models.CharField(max_length=500)

    def __str__(self):
        return self.contest.title_in_english + " contest -> image " + str(self.pk)


class Staff(models.Model):
    STAFF_FIELD = (('t', 'technical'), ('s', 'scientific'), ('e', 'executive'))
    STAFF_TYPE = (('m', 'manager'), ('e', 'employee'))
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    name_in_english = models.CharField(max_length=200)
    name_in_persian = models.CharField(max_length=200)
    part = models.CharField(max_length=30, choices=STAFF_FIELD)
    type = models.CharField(max_length=30, choices=STAFF_TYPE)
    image = models.ImageField(upload_to=path_and_rename, blank=True)

    def __str__(self):
        return self.contest.title_in_english + " contest -> " + self.name_in_english


class Resourse(models.Model):
    title_in_english = models.CharField(max_length=200)
    title_in_persian = models.CharField(max_length=200)
    description_in_english = models.CharField(max_length=500, null=True)
    description_in_persian = models.CharField(max_length=500, null=True)
    file = models.FileField(upload_to=path_and_rename)

    def __str__(self):
        return self.title_in_english


class BlogCategorie(models.Model):
    title_in_english = models.CharField(max_length=200)
    title_in_persian = models.CharField(max_length=200)

    def __str__(self):
        return self.title_in_english


class BlogPost(models.Model):
    blog_categorie = models.ForeignKey(BlogCategorie, on_delete=models.CASCADE)
    title_in_english = models.CharField(max_length=200)
    title_in_presian = models.CharField(max_length=200)
    cover_in_english = models.ImageField(upload_to=path_and_rename)
    cover_in_persian = models.ImageField(upload_to=path_and_rename)
    summery_in_english = models.TextField(max_length=300)
    summery_in_persian = models.TextField(max_length=300)
    content_in_english = RichTextField()
    content_in_persian = RichTextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.blog_categorie.title_in_english + " -> " + self.title_in_english


class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=500)
    content = models.TextField()

    def __str__(self):
        return self.name
