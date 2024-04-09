from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Art, Style, Medium, Comment

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# Model 1: Art
class ArtList(ListView):
    model = Art

class ArtDetail(DetailView):
    model = Art

class ArtCreate(CreateView):
    model = Art
    fields =['title', 'image', 'description', 'price', 'style', 'medium']

class ArtUpdate(UpdateView):
    model = Art
    fields = ['title', 'image', 'description', 'price', 'style', 'medium']

# class ArtDelete(DeleteView):
#     model = Art
#     success_url = '/art'

class ArtDelete(DeleteView):
    model = Art
    success_url = reverse_lazy('/art')
    
# Model 2: Style
class StyleList(ListView):
    model = Style

class StyleDetail(DetailView):
    model = Style

class StyleUpdate(UpdateView):
    model = Style
    fields = '__all__'

class StyleDelete(DeleteView):
    model = Style
    success_url = '/style'

# Model 3: Medium
class MediumList(ListView):
    model = Medium

class MediumDetail(DetailView):
    model = Medium

class MediumUpdate(UpdateView):
    model = Medium
    fields = '__all__'

class MediumDelete(DeleteView):
    model = Medium
    success_url = '/medium'

# Model 4: Comment
class CommentList(ListView):
    model = Comment

class CommentDetail(DetailView):
    model = Comment

class CommentCreate(CreateView):
    model = Comment
    fields = '__all__'

class CommentUpdate(UpdateView):
    model = Comment
    fields = '__all__'

class CommentDelete(DeleteView):
    model = Comment
    success_url = '/comment'

# let's go team