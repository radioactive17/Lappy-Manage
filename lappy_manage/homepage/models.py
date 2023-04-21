from django.db import models
from django.urls import reverse
from PIL import Image

class LaptopO(models.Model):
    laptop_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=255)
    rating = models.FloatField()
    price = models.IntegerField()
    images = models.ImageField(default = 'nia.jpg', upload_to= 'homepage/images')

    def __str__(self):
        return str(self.laptop_id)
    
    def get_absolute_url(self):
        return reverse('explore')

    def save(self):
        super().save()
        img = Image.open(self.images.path)
        # if img.height > 300 or img.width > 300:
        output_size = (300,300)
        img.thumbnail(output_size)
        img.save(self.images.path)

class LaptopD(models.Model):
    laptop = models.ForeignKey('LaptopO', on_delete=models.CASCADE)
    accessories = models.CharField(max_length = 255)
    model_number = models.CharField(max_length=255)
    series = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    type_of_laptop = models.CharField(max_length=255)
    suitable_for = models.CharField(max_length=255) 
    power = models.CharField(max_length=255)
    graphics_memory_type = models.CharField(max_length=255)
    graphics_memory_capacity = models.CharField(max_length=255)
    processor_name = models.CharField(max_length=255)
    processor_generation = models.CharField(max_length=255)
    ssd = models.CharField(max_length=255)
    ssd_capacity = models.CharField(max_length=255)
    ram = models.CharField(max_length=255)
    ram_type = models.CharField(max_length=255)
    clock_speed = models.CharField(max_length=255)
    expandable_memory = models.CharField(max_length=255)
    graphics_processor = models.CharField(max_length=255)
    number_of_cores = models.CharField(max_length=255)

    def __str__(self):
        return str(self.laptop)