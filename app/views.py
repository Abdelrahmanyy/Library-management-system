from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
# Create your views here.


def index(request):
    if request.method == 'POST':
        add_book = bookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()

    if request.method == 'POST':
        add_category = categoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()


    context = {
        'categories':category.objects.all(),
        'books':book.objects.all(),
        'form':bookForm(),
        'formcat':categoryForm(),
        'books_count':book.objects.count(),
        'available_books':book.objects.filter(status='available').count(),
        'rental_books':book.objects.filter(status='rental').count(),
        'sold_books':book.objects.filter(status='sold').count(),

    }
    return render(request, 'pages/index.html', context)



def books(request):
    search = book.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)


    context = {
        'categories':category.objects.all(),
        'books':search,
        'formcat':categoryForm(),
    }
    return render(request, 'pages/books.html', context)    


def update(request, id):
    book_id = book.objects.get(id=id)
    if request.method == 'POST':
        book_save = bookForm(request.POST, request.FILES, instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save = bookForm(instance=book_id)        
    context = {
        'form':book_save,
    }
    return render(request, 'pages/update.html', context)
    
def delete(request, id):
    book_delete = get_object_or_404(book, id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/')
    return render(request, 'pages/delete.html')
    
