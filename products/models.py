import random
import os
from django.db import models


def get_filename_ext(file_path):
    base_name = os.path.basename(file_path)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 123456789)
    name, ext = get_filename_ext(filename)
    upload_filename = f'{new_filename}{ext}'
    return f'products/{new_filename}/{upload_filename}'


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2,
                                max_digits=20,
                                default=3.30)
    image = models.ImageField(upload_to=upload_image_path,
                              null=True,
                              blank=False)

    def __str__(self):
        return self.title
