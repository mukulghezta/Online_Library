from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, CD
from .forms import CreateBook, CreateCD
from django.contrib.auth.decorators import login_required
from reserve.models import BookReserve
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Count


# HOME PAGE
def home(request):
    if request.user.is_authenticated:
        books = Book.objects.all()
        cds = CD.objects.all()
        logged_in_user = get_object_or_404(User, username=str(request.user))
        return render(request, 'books_cds/home.html', {'books':books, 'cds':cds, 'logged_in_user':logged_in_user})
    else:
        books = Book.objects.all()
        cds = CD.objects.all()
        return render(request, 'books_cds/home.html', {'books':books, 'cds':cds})



# VIEW BOOK    
def book_detail(request, book_id):
    book = Book.objects.get(book_id = book_id)
    return render(request, 'books_cds/book_detail.html', {'book':book})

# VIEW CD   
def cd_detail(request, cd_id):
    cd = CD.objects.get(cd_id = cd_id)
    return render(request, 'books_cds/cd_detail.html', {'cd':cd})



# ADD BOOK
@login_required(login_url="/accounts/login/")
def book_add(request):
    if request.method == "POST":
        form = CreateBook(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books_cds:home')
    else:
        form = CreateBook()
    return render(request, 'books_cds/book_add.html', {'form':form})

# ADD CD
@login_required(login_url="/accounts/login/")
def cd_add(request):
    if request.method == "POST":
        form = CreateCD(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books_cds:home')
    else:
        form = CreateCD()
    return render(request, 'books_cds/cd_add.html', {'form':form})



# UPDATE BOOK
@login_required(login_url="/accounts/login/")
def book_edit(request, book_id):
    book = Book.objects.get(book_id = book_id)
    form = CreateBook(instance=book)

    if request.method == "POST":
        form = CreateBook(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books_cds:home')
    return render(request, 'books_cds/book_add.html', {'form':form})

# UPDATE CD
@login_required(login_url="/accounts/login/")
def cd_edit(request, cd_id):
    cd = CD.objects.get(cd_id = cd_id)
    form = CreateCD(instance=cd)

    if request.method == "POST":
        form = CreateCD(request.POST, instance=cd)
        if form.is_valid():
            form.save()
            return redirect('books_cds:home')
    return render(request, 'books_cds/cd_add.html', {'form':form})



# DELETE BOOK
@login_required(login_url="/accounts/login/")
def book_delete(request, book_id):
    book = Book.objects.get(book_id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('books_cds:home')
    return render(request, 'books_cds/book_delete.html', {'book':book})

# DELETE CD
@login_required(login_url="/accounts/login/")
def cd_delete(request, cd_id):
    cd = CD.objects.get(cd_id=cd_id)
    if request.method == "POST":
        cd.delete()
        return redirect('books_cds:home')
    return render(request, 'books_cds/cd_delete.html', {'cd':cd})
    