from django.db import models
# from django.contrib.auth.models import User
from users.models import User
from django.urls import reverse


class Community(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField (blank=False, null=False)
    image = models.ImageField(
        'Imagen',
        upload_to='Entry',
    )
    slug = models.SlugField(max_length=255, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user',)
    verify = models.BooleanField(default=True)

    def get_url(self):
        return reverse('comunidad_detail', args=[self.slug])

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Community'
        verbose_name_plural = 'Communities'
        ordering = ['name']



