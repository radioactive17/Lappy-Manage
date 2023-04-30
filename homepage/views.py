from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import LaptopO, LaptopD
import pandas as pd
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from datetime import datetime
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserRegistrationForm, LaptopDForm, AddLaptopO, AddLaptopD
from django.core.paginator import Paginator

def home(request):
    laptopo = LaptopO.objects.all().order_by('laptop_id')[:12]
    context = {
         'laptopo': laptopo,
     }
    
    return render(request, 'homepage/home.html', context)

def explore(request):
    try:
        try:
            laptopo = LaptopO.objects.filter(name__icontains =request.GET.get('search'))
        except:
            sort_by = request.GET.get('sort')
            if sort_by == 'l2h':
                laptopo = LaptopO.objects.all().order_by('price')
            elif sort_by == 'h2l':
                laptopo = LaptopO.objects.all().order_by('-price')
            elif sort_by == 'rating':
                laptopo = LaptopO.objects.all().order_by('-rating')
        paginator = Paginator(laptopo, 20)  # Show 25 contacts per page.
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
    except:
        laptopo = LaptopO.objects.all()
        paginator = Paginator(laptopo, 20)  # Show 25 contacts per page.
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
    return render(request, "homepage/explore.html", {"page_obj": page_obj})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email_id = form.cleaned_data.get('email')
            messages.success(request, f'Welcome to Lappy Manage, {email_id}. You can now Log In using your set username and password')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'homepage/register.html', {'form':form})

class DetailLaptopView(DetailView):
    model = LaptopD
    template_name = 'homepage/detailed.html'

    def get_object(self, *args, **kwargs):
        return LaptopD.objects.get(laptop = self.kwargs['pk']) 
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['laptopo'] = LaptopO.objects.get(laptop_id = self.kwargs['pk'])
        return context

class DeleteLaptopView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = LaptopO
    context_object_name = 'laptopo'
    success_url = '/explore/'
    success_message = 'Laptop details deleted successfully'
    
    def test_func(self):
        laptopo = self.get_object()
        if self.request.user.is_superuser:
            return True
        return False

class UpdateLaptopOView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = LaptopO
    fields = '__all__'
    success_message = 'LaptopO details updated successfully'
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("update2-laptop", kwargs={"pk": pk})
    

class UpdateLaptopDView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = LaptopD
    form_class = LaptopDForm
    success_message = 'LaptopD details updated successfully'
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False
    
    def get_object(self, *args, **kwargs):
        return LaptopD.objects.get(laptop = self.kwargs['pk']) 
    
    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("laptop-details", kwargs={"pk": pk})
    

def add_laptopo_data(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = AddLaptopO(request.POST)
            if form.is_valid():
                form.save()
                laptopo = LaptopO.objects.filter().order_by('-laptop_id')[0]
                messages.success(request, f'{laptopo.name} successfully added to the database!')
                # laptopd = LaptopD(laptop = laptopo)
                # laptopd.save()
                return redirect('new2-laptop')
        else:
            form = AddLaptopO()
        return render(request, 'homepage/new_laptopo.html', {'form':form})

def add_laptopd_data(request, *args, **kwargs):
    laptopo = LaptopO.objects.filter().order_by('-laptop_id')[0]
    if request.user.is_superuser:
        if request.method == 'POST':
            form = AddLaptopD(request.POST, initial = {'laptop': laptopo})
            if form.is_valid():
                form.save()
                model_number = form.cleaned_data.get('model_number')
                messages.success(request, f'{model_number} successfully added to the database!')
                return redirect('explore')
        else:
            form = AddLaptopD(initial = {'laptop': laptopo})
    return render(request, 'homepage/new_laptopd.html', {'form': form})