from django.db import models

from django.utils import timezone
from django.forms.models import inlineformset_factory
class UserPersonalDetails(models.Model):
    gender_type_choice = (
        ('M','Male'),
        ('F','Female'),
        ('O','Other')
    )
    user_type_choice = (
        ('A', 'Authorized'),
        ('UA', 'UnAuthorized'),
        ('A', 'Admin'),
        ('Z', 'SuperAdmin'),
    )
    uniqueId = models.CharField(max_length=100,null=True,blank=True)
    dateCreated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    firstName = models.CharField(max_length=100,null=True,blank=True)
    lastName = models.CharField(max_length=100,null=True,blank=True)
    middleName = models.CharField(null=True,blank=True,max_length=250)
    dob = models.DateField(blank=True,null=True)
    gender = models.CharField(null=True,blank=True,choices=gender_type_choice,max_length=1)



    class Meta:
        db_table='user_details'



class p_laptop(models.Model):
    l_name=models.CharField(max_length=100)
    l_rating=models.CharField(max_length=100)
    l_price=models.CharField(max_length=100)

    class Meta:
        db_table='p_laptop'

class d_laptop(models.Model):
    l_Id = models.ForeignKey(p_laptop,on_delete=models.CASCADE,null=False,primary_key=True)
    l_includes=models.CharField(max_length=100,null=True)
    l_model_number=models.CharField(max_length=100,null=True)
    l_series=models.CharField(max_length=100,null=True)
    l_color=models.CharField(max_length=100,null=True)
    l_type=models.CharField(max_length=100,null=True)
    l_suitable=models.CharField(max_length=100,null=True)
    l_power=models.CharField(max_length=100,null=True)
    l_gm_type=models.CharField(max_length=100,null=True)
    l_gm_capacity=models.CharField(max_length=100,null=True)
    l_processor_name=models.CharField(max_length=100,null=True)
    l_processor_generation=models.CharField(max_length=100,null=True)
    l_ssd=models.CharField(max_length=100,null=True)
    l_ssd_capacity=models.CharField(max_length=100,null=True)
    l_ram=models.CharField(max_length=100,null=True)
    l_ram_type=models.CharField(max_length=100,null=True)
    l_clock_speed=models.CharField(max_length=100,null=True)
    l_expandable_memory=models.CharField(max_length=100,null=True)
    l_graphic_processor=models.CharField(max_length=100,null=True)
    l_number_cores=models.CharField(max_length=100,null=True)
    created_at = models.DateTimeField(default=timezone.now, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True, default=timezone.now)
    def __str__(self) :
        return (self.l_Id.l_name)

    class Meta:
        db_table='d_laptop'

