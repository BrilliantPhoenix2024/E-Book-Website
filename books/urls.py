from django.urls import path, include

from .views import BookListView, book_detail_view, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', book_detail_view, name='book_detail'),
    path('new/', BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/edit/', BookUpdateView.as_view(), name='book_update'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
]


