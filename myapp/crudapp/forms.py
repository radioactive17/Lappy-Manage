from django.forms import ModelForm
from .models import p_laptop,d_laptop
from django.forms.models import inlineformset_factory
class LaptopForm1(ModelForm):
    class Meta:
        model =p_laptop
        fields ='__all__'

class LaptopForm2(ModelForm):
    class Meta:
        model =d_laptop
        fields = [field.name for field in d_laptop._meta.fields if field.name != 'l_Id']
