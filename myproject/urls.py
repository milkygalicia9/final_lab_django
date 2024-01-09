# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from myapp.views import HomeView, AboutView, BookListView, BookDetailView, BookUpdateView, BookDeleteView, BookCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'), 
    path('books/<int:pk>/edit/', BookUpdateView.as_view(), name='book_confirm_edit'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book_confirm_delete'),  
    path('books/create/', BookCreateView.as_view(), name='book_create'), 
    path('about/', AboutView.as_view(), name='about'),
    path('', include('myapp.urls')),
]
