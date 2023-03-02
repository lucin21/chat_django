from django.db import models
from django.db.models import SET_NULL
from users.models import User
from comunity.models import Community


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    miniature = models.ImageField(upload_to='posts/images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    community = models.ForeignKey(Community, on_delete=SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)


    def __str__(self):
        return self.title
