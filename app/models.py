from django.db import models
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField 

# Create your models here.


class Course(models.Model):
    course_name = models.CharField('Kurs nomi' , max_length=50)
    count_module  = models.IntegerField('Modullar soni' )
    image = models.ImageField('Rasm', upload_to="course_img/")

    
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = "Courses"

        
    def __str__(self):
        return self.course_name


class Category_blog(models.Model):
    title = models.CharField('Sarlavha',max_length=255)
    slug = models.SlugField('Manzil',max_length=255, unique=True)

    class Meta:
        verbose_name = 'Category_blog'
        verbose_name_plural = "Categories_blog"

    def get_absolute_url(self):
        return f"/category/{self.slug}/"
        
    def __str__(self):
        return self.title



class Blog(models.Model):
    title = models.CharField('Sarlavha',max_length = 50)
    img = models.ImageField('Rasm', upload_to="blog_img/")
    description = models.TextField('Blog')
    category_blog = models.ForeignKey(Category_blog , on_delete=models.CASCADE)
    date = models.DateTimeField('Sana' , default=timezone.now)
    like = models.IntegerField('Like' , default=0)
    dislike = models.IntegerField('Dislike' , default=0)
    popular = models.IntegerField('Ko\'rilganlar soni' , default=0)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = "Blogs"

    def get_absolute_url(self):
        return f"/blog/{self.id}/"

    def __str__(self):
        return self.title
