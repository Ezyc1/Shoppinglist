from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from .models import List, Item
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView

# Create your views here.
class AllaListor(LoginRequiredMixin, ListView):
    model = List
    template_name = 'listor/hem.html'
    context_object_name = 'listor'
    ordering = ['created_date']
    
class EnLista(LoginRequiredMixin, ListView):
    model=Item
    template_name = 'listor/lista.html'
    context_object_name = 'items'
    
    def get_queryset(self):
        return Item.objects.filter(list=self.kwargs['pk'])
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['listan'] = List.objects.filter(id=self.kwargs['pk'])
        return context
    
class NyLista(LoginRequiredMixin, CreateView):
    model = List
    fields = ['list_name']
    template_name = 'listor/list_form.html'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['status'] = {'status':'Ny'}
        return context
    
    def form_valid(self,form):
        form.instance.list_user=self.request.user
        return super().form_valid(form)
    
class UppdateraLista(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = List
    fields = ['list_name']
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['status'] = {'status':'Uppdatera'}
        return context
    
    def test_func(self):
        lista=self.get_object()
        if self.request.user == lista.list_user:
            return True
        return False
    
class NyVara(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['item_name', 'amount']
    template_name = 'listor/item_form.html'
    
    def form_valid(self,form):
        form.instance.list=get_object_or_404(List,id=self.kwargs.get('pk'))
        return super().form_valid(form)
    