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
    accessories = models.CharField(max_length = 255, default = 'No description available')
    model_number = models.CharField(max_length=255, default = 'No description available')
    series = models.CharField(max_length=255, default = 'No description available')
    color = models.CharField(max_length=255, default = 'No description available')
    type_of_laptop = models.CharField(max_length=255, default = 'No description available')
    suitable_for = models.CharField(max_length=255, default = 'No description available') 
    power = models.CharField(max_length=255, default = 'No description available')
    graphics_memory_type = models.CharField(max_length=255, default = 'No description available')
    graphics_memory_capacity = models.CharField(max_length=255, default = 'No description available')
    processor_name = models.CharField(max_length=255, default = 'No description available')
    processor_generation = models.CharField(max_length=255, default = 'No description available')
    ssd = models.CharField(max_length=255, default = 'No description available')
    ssd_capacity = models.CharField(max_length=255, default = 'No description available')
    ram = models.CharField(max_length=255, default = 'No description available')
    ram_type = models.CharField(max_length=255, default = 'No description available')
    clock_speed = models.CharField(max_length=255, default = 'No description available')
    expandable_memory = models.CharField(max_length=255, default = 'No description available')
    graphics_processor = models.CharField(max_length=255, default = 'No description available')
    number_of_cores = models.CharField(max_length=255, default = 'No description available')

    def __str__(self):
        return str(self.laptop)