from django.db import models

# Create your models here.
class Reply(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    selected = models.PositiveSmallIntegerField()

    def answer(self):
        self.save()

    def __str__(self):
        return str(self.author)
