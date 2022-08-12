from django.db import models
from account.models import User
from froala_editor.fields import FroalaField
from django.urls import reverse


#post viewcount
class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Author(models.Model):
    user = models.OneToOneField(User,related_name='is_author', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Post(models.Model): 
    thumbnail = models.ImageField()
    title = models.CharField(max_length=100)
    overview = models.TextField()
    content = FroalaField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # commentCount = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, blank=True, related_name='cat')
    featured = models.BooleanField(default=False)
    previous_post = models.ForeignKey('self', related_name='prev_post', on_delete=models.SET_NULL, blank = True, null=True)
    next_post = models.ForeignKey('self', on_delete=models.SET_NULL, blank = True, null=True, related_name='nxt_post')


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-id']    

    @property
    def get_comments(self):
        return self.comments.all()

    def get_update_url(self):
        return reverse('post_update', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('post_delete', kwargs={'id': self.id})

    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()

    @property
    def commentCount(self):
        return Comment.objects.filter(post=self).count()



