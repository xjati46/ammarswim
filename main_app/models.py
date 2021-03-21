from django.db import models

# Create your models here.


class Newsfeed(models.Model):
    judul = models.CharField(max_length=30)
    waktu_post = models.DateField(auto_now_add=True, null=True, blank=True)
    konten = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.judul} | {self.waktu_post}'

    class Meta:
        ordering = ['-waktu_post']