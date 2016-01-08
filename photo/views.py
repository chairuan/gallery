from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from photo.models import Photo,Item

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"
 
    def get_context_data(self,**kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        context['item_list'] = Item.objects.all()
        return context

class ItemListView(ListView):
    template_name = "items_list.html"
    model = Item
    context_object_name = 'items_list'

    def get_context_data(self,**kwargs):
        context = super(ItemListView,self).get_context_data(**kwargs)
        return context

class ItemDetailView(DetailView):
    template_name = "items_detail.html"
    model = Item
    context_object_name = 'item'

    def get_context_data(self,**kwargs):
        context = super(ItemDetailView,self).get_context_data(**kwargs)
        return context

class PhotoDetailView(DetailView):
    template_name = "photo_detail.html"
    model = Photo
    context_object_name = 'photo'

    def get_context_data(self,**kwargs):
        context = super(PhotoDetailView,self).get_context_data(**kwargs)
        return context

