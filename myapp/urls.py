from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView # Correct the import statement

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/new/', BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/edit/', BookUpdateView.as_view(), name='book_confirm_edit'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book_confirm_delete'),
    
    # Add other URLs as needed
]
