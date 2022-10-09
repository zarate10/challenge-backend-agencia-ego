from django.db import models
import os 


# Create your models here.

CATEGORY_CHOICES = (
    ("1", "Autos"),
    ("2", "Pickups y Comerciales"),
    ("3", "SUVs y Crossovers"),
)

class Car(models.Model): 
    name = models.CharField(max_length=64)
    category = models.CharField(max_length=64, choices=CATEGORY_CHOICES, default='1')
    title = models.CharField(max_length=64, blank=True)
    description = models.TextField(blank=True)
    year = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to="profile_car", null=True)


    def delete(self, *args, **kwargs): 
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)

        super(Car, self).delete(*args, **kwargs)

    def __str__(self):
        return self.name

class Caracteristicas(models.Model): 
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=200, blank=True)
    image_url = models.URLField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.car.name}'

class Destacados(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    image_url =  models.URLField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.car.name}'