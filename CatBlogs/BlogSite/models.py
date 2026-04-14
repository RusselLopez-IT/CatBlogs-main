from django.db import models

# Create your models here.
class Cat(models.Model):
    cat_picture = models.ImageField(upload_to='static/cat_pics', blank=True, null=True)
    breed = models.CharField(max_length=100)
    description = models.TextField()
    traits = models.TextField()
    height = models.CharField(max_length=100) 
    weight = models.CharField(max_length=100) 
    population = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Cat'
        verbose_name_plural = 'Cats'

    def __str__(self):
        return self.breed