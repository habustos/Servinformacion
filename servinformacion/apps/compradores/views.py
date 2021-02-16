from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms

#from .forms import *
from .models import *


class List(ListView):
    model = compradores

class Create(SuccessMessageMixin, CreateView):

    model = compradores
    form = compradores
    fields = "__all__"
    success_message = 'Cliente Creado Correctamente !'

    def get_success_url(self):
        return reverse('list')

class Details(DetailView):
    model = compradores


class Edit(SuccessMessageMixin, UpdateView):

    model = compradores
    form = compradores
    fields = "__all__"
    success_message = 'Cliente actualizado correctamente !'

    def get_success_url(self):
        return reverse('list')

class Delete(SuccessMessageMixin, DeleteView):
    model = compradores
    form = compradores
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Cliente eliminado correctamente !'
        messages.success(self.request, (success_message))
        return reverse('list')
