from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render

from .models import Book


class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    template_name = 'books/book_list.html'
    context_object_name = 'books'


# class BookDetailView(generic.DetailView):
#     model = Book
#     template_name = 'books/book_detail.html'
def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book_comment = book.comments.all()
    return render(request, 'books/book_detail.html', {'book': book, 'comment': book_comment})


class BookCreateView(generic.CreateView):
    model = Book
    fields = ['title', 'author', 'content', 'price', 'cover']
    template_name = 'books/book_create.html'


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'content', 'cover']
    template_name = 'books/book_update.html'


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')


