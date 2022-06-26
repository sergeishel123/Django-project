from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    user_rating = models.IntegerField(default = 0)
    @staticmethod
    def update_rating(self,auth):
         summ1 = 0
         for article_rating in auth.articles:
             article_rating *= 3
             summ1 += article_rating
         summ2 = 0
         for comment_rating in auth.comments_rating:
             summ2 += comment_rating
         summ3 = 0
         for to_comment_rating in auth.to_comments_rating:
             summ3 += to_comment_rating
         self.user_rating = summ1 + summ2 + summ3




class Category(models.Model):
    name = models.CharField(max_length = 255,unique = True)

array = [('N','News'), ('A','Article')]
class Post(models.Model):
    author_post = models.ForeignKey(Author,on_delete = models.CASCADE)
    type = models.CharField(max_length = 1,choices = array)
    time_in = models.DateTimeField(auto_now_add = True)
    category_post = models.ManyToManyField(Category,through = 'PostCategory')
    heading = models.CharField(max_length = 255)
    text = models.TextField()
    rating = models.IntegerField(default = 0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.text[:124]}...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post,on_delete = models.CASCADE)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete = models.CASCADE)
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    text = models.TextField()
    time_in = models.DateTimeField(auto_now_add = True)
    rating = models.IntegerField(default = 0)

    def like(self):
        self.rating += 1
        self.save()
    def dislike(self):
        self.rating -= 1
        self.save()








# Create your models here.
