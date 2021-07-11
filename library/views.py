from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import *
from django.views.generic.detail import DetailView
from datetime import date
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    books = Book.objects.all()
    return render(request, 'library/home.html', {'books': books})

class book_detail(DetailView):
    template_name = 'library/book_desc.html'
    model = Book

@login_required()
def profile(request):
    user = request.user
    student = Student.objects.get(user=user)
    borrower = Borrower.objects.filter(user=user)
    return render(request, 'library/profile.html', {'student': student, 'Borrower': borrower})

@login_required()
def book_issue(request, pk):
    user = request.user
    book = Book.objects.get(id=pk)
    borrower = Borrower(user=user, book=book, issue_date=date.today(), return_date=date.today())
    borrower.save()
    Book.objects.filter(id=pk).update(available_copies=book.available_copies-1)
    # update total books due in student model
    s = Student.objects.get(user=user)
    s.total_books_Due += 1
    s.save()

    return HttpResponseRedirect('/profile/')

@login_required()
def book_return(request, pk, id):
    user = request.user
    # books available update
    b = Book.objects.get(id=pk)
    b.available_copies += 1
    b.save()

    # delete the borrower record
    borrower = Borrower.objects.get(id=id)
    borrower.delete()

    # student book_due update
    s = Student.objects.get(user=user)
    s.total_books_Due -= 1
    s.save()

    return HttpResponseRedirect('/profile/')