from django.shortcuts import render,redirect
from django.db.models import Q
from django.http import HttpResponse
from crudapp.forms import LaptopForm1,LaptopForm2
from .models import p_laptop,d_laptop
from django.http import JsonResponse
def home(request):
    context={}
    return render(request, 'crudapp/index.html',context)


def create_laptop(request):
    form=LaptopForm1()
    sform=LaptopForm2()
    if request.method=='POST':
        form=LaptopForm1(request.POST)
        sform=LaptopForm2(request.POST)

        if form.is_valid() and sform.is_valid() :
            pm_instance=form.save()
            sm_instance=sform.save(commit=False)
            print(pm_instance.id)
            sm_instance.l_Id=pm_instance
            sm_instance.save()
            print('Success')
            return redirect('crud_page')
    context={'form':form,'sform':sform}
    return render(request,'crudapp/student.html',context)




def show_laptop(request):
    laptops=p_laptop.objects.all() 
    context={'laptops':laptops}
    return render(request,'crudapp/crud_page.html',context)

def show_all_data(request,id):
    if request.method=="GET":
        pdata=p_laptop.objects.get(id=id)
        print(pdata.id)
        ddata=d_laptop.objects.get(l_Id__id=id)
        print(ddata.l_model_number)
        context={'pdata':pdata,'ddata':ddata}
    return render(request,'crudapp/show_all.html',context)


def delete_laptop(request,id):
    laptop_val = p_laptop.objects.get(id=id)  
    laptop_val.delete()  
    return redirect("crud_page")


def update_laptop(request, id):
    laptop_val = p_laptop.objects.get(id=id)
    laptop_val_2=d_laptop.objects.get(l_Id__id=id)
    if request.method == 'POST':
        form = LaptopForm1(request.POST, instance=laptop_val)
        sform = LaptopForm2(request.POST,instance=laptop_val_2)
        if form.is_valid() and sform.is_valid():
            form.save()
            sform.save()
            return redirect('crud_page')
    else:
        form = LaptopForm1(instance=laptop_val)
        sform =LaptopForm2(instance=laptop_val_2)

    return render(request,
                'crudapp/student.html',
                {'form': form,'sform':sform})