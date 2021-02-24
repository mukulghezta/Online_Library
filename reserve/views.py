from django.shortcuts import render, redirect, get_object_or_404
from .models import BookReserve, CDReserve
from books_cds.models import Book, CD
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.contrib import messages
from django.db.models import Count
from django.contrib.auth.decorators import login_required


@login_required(login_url="/accounts/login/")
def allreserves(request):
    if request.user.is_superuser:
        bookreserves = BookReserve.objects.all()
        cdreserves = CDReserve.objects.all()
        logged_in_user = get_object_or_404(User, username=str(request.user))
        return render(request, 'reserve/allreserves.html', {'bookreserves':bookreserves, 'cdreserves':cdreserves, 'logged_in_user':logged_in_user})
    else:
        messages.info(request,"You are not allowed to view this page!!!")
        return redirect('reserve:myreserves')


@login_required(login_url="/accounts/login/")
def myreserves(request):
    # get the logged in user's username
    logged_in_user = get_object_or_404(User, username=str(request.user))
    
    # getting book and cd records of logged in user
    bookreserves = BookReserve.objects.filter(user_id=logged_in_user)
    cdreserves = CDReserve.objects.filter(user_id=logged_in_user)

    # getting number of book and cd records of logged in user in dictionary format
    book_dict_items = BookReserve.objects.filter(user_id=logged_in_user).aggregate(Count('user_id'))
    cd_dict_items = CDReserve.objects.filter(user_id=logged_in_user).aggregate(Count('user_id'))

    # getting number of book and cd records of logged in user
    total_book_items = book_dict_items["user_id__count"]
    total_cd_items = cd_dict_items["user_id__count"]

    bookduedates = BookReserve.objects.filter(user_id=logged_in_user).only("due_date")

    days_left_to_return_book = 0
    bookpastduedates = 0
    for i in bookduedates:
        a=i.due_date
        b=i.reserve_date
        c=a-b
        days_left_to_return_book=c.days
        if days_left_to_return_book < 0:
            bookpastduedates = bookpastduedates + 1
    
    days_left_to_return_cd = 0
    cdpastduedates = 0
    cdduedates = CDReserve.objects.filter(user_id=logged_in_user).only("due_date")
    for j in cdduedates:
        d=j.due_date
        e=j.reserve_date
        f=d-e
        days_left_to_return_cd=f.days
        if cdpastduedates < 0:
            cdpastduedates = cdpastduedates + 1

    # bookduebooks = BookReserve.objects.filter(user_id=logged_in_user).only("due_date")

    return render(request, 'reserve/myreserves.html', {'bookreserves':bookreserves, 'total_book_items':total_book_items, 'cdreserves':cdreserves, 'total_cd_items':total_cd_items, 'logged_in_user':logged_in_user, 'days_left_to_return_book':days_left_to_return_book, 'days_left_to_return_cd':days_left_to_return_cd, 'bookpastduedates':bookpastduedates, 'cdpastduedates':cdpastduedates})


# @login_required(login_url="/accounts/login/")
def createreserve(request, book_id):
    book = Book.objects.get(book_id=book_id)
    logged_in_user = get_object_or_404(User, username=str(request.user))
    dict_items = BookReserve.objects.filter(user_id=logged_in_user).aggregate(Count('user_id'))
    total_items = dict_items["user_id__count"]

    # a = BookReserve.objects.filter(user_id=logged_in_user)

    book.book_quantity
    if request.method == "POST":
        if total_items == 2 or total_items > 2:
            messages.info(request,"Cannot reserve! You have already reserved two books.")
            return redirect('books_cds:home')
        else:
            a = BookReserve()
            a.user_id = logged_in_user
            a.book_id = book
            a.reserve_date = datetime.now()
            a.due_date = datetime.now() + timedelta(days=14)
            a.save()
            # book.book_quantity = book.book_quantity - 1
            messages.info(request,"Book reserve done!")
            return redirect('books_cds:home')

    return render(request, 'reserve/createreserve.html', locals())


# @login_required(login_url="/accounts/login/")
def createcdreserve(request, cd_id):
    cd = CD.objects.get(cd_id=cd_id)
    logged_in_user = get_object_or_404(User, username=str(request.user))
    dict_items = CDReserve.objects.filter(user_id=logged_in_user).aggregate(Count('user_id'))
    total_items = dict_items["user_id__count"]

    if request.method == "POST":
        if total_items == 2 or total_items > 2:
            messages.info(request,"Cannot reserve! You have already reserved two CDs.")
            return redirect('books_cds:home')
        else:
            a = CDReserve()
            a.user_id = logged_in_user
            a.cd_id = cd
            a.reserve_date = datetime.now()
            a.due_date = datetime.now() + timedelta(days=14)
            a.save()
            messages.info(request,"CD reserve done!")
            return redirect('books_cds:home')

    return render(request, 'reserve/createcdreserve.html', locals())


def releasereserve(request, id):
    bookreserve = BookReserve.objects.get(id=id)
    if request.method == "POST":
        bookreserve.delete()
        return redirect('reserve:myreserves')
    return render(request, 'reserve/releasereserve.html', {'bookreserve':bookreserve})


def releasecdreserve(request, id):
    cdreserve = CDReserve.objects.get(id=id)
    if request.method == "POST":
        cdreserve.delete()
        return redirect('reserve:myreserves')
    return render(request, 'reserve/releasecdreserve.html', {'cdreserve':cdreserve})
