# myapp/views.py
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView,  CreateView, UpdateView, DeleteView
from .models import Book
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'
    paginate_by = 3 

    def get_queryset(self):
        return Book.objects.all()

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Access the 'page' GET parameter
        page = self.request.GET.get('page', 1)
        context['page'] = page
        context['page'] = page
        context['books'] = context['object_list']  
        return context

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any additional context data here
        context['book'] = Book.objects.get(pk=self.kwargs['pk'])  # Adjust this line based on your model structure
        return context
class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html' 

class BookCreateView(CreateView):
    model = Book
    template_name = 'book_form.html'
    fields = ['title', 'authors', 'publication_date']
    success_url = reverse_lazy('book_list')

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book_confirm_edit.html'
    fields = ['title', 'authors', 'publication_date']
    

    def form_valid(self, form):
        response = super().form_valid(form)
        # Additional logic if needed
        return response
    
    
    def get_success_url(self):
        # Redirect to the book list page after successfully updating the book
        return reverse_lazy('book_list') 
    
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book_list')

