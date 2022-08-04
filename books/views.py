from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from books.models import Book


def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, template, context)


def show_book(request, pub_date):
    template = 'books/book.html'
    book = get_object_or_404(Book, pub_date=pub_date)
    context = {
        'book': book,

    }
    return render(request, template, context)





