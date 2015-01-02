from django.shortcuts import render
from django.views.generic import ListView
from .models import Link

class LinkListView(ListView):
	model = Link