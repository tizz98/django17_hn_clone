from django.shortcuts import render
from django.views.generic import ListView

class LinkListView(ListView):
	model = Link