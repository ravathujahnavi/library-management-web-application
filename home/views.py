from django.shortcuts import render, HttpResponse
import requests
from .models import Books,Members
from django.db.models import Q

# Create your views here.

def index(request):
    # return HttpResponse("this is home page")
    # dictionary - we fetch values from database and send it to template to display us
    return render(request, 'index.html')


# BOOKS PAGE FUCTIONS

def books(request):
    search_url = 'https://frappe.io/api/method/frappe-library'
    response = requests.get(search_url)
    data = response.json()["message"]
    for book in data:
        if not Books.objects.filter(title=book["title"], authors=book["authors"], isbn=book["isbn"]).exists:
            Books.objects.create(title=book["title"], authors=book["authors"], isbn=book["isbn"], publisher=book["publisher"])
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(title__icontains=q) | Q(authors__icontains=q))
        books = Books.objects.filter(multiple_q)
    else:
        books = Books.objects.all()
    return render(request, 'books.html', {'books' : books })

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        authors = request.POST['authors']
        isbn = request.POST['isbn']
        publisher = request.POST['publisher']
        book = Books(title=title,authors=authors,isbn=isbn,publisher=publisher)
        book.save()
    else:
        pass
    books = Books.objects.all()
    return render(request, 'books.html', {'books' : books })

def delete_book(request,myid):
    book = Books.objects.get(id=myid)
    book.delete()
    books = Books.objects.all()
    return render(request, 'books.html', {'books' : books })


# MEMBERS PAGE FUNCTIONS
def members(request):
    members = Members.objects.all()
    return render(request, 'members.html', {'members' : members })

def add_member(request):
    if request.method == 'POST':
        name = request.POST['name']
        member = Members(name = name)
        member.save()
    else:
        pass
    members = Members.objects.all()
    return render(request, 'members.html', {'members' : members })

def delete_member(request,myid):
    member = Members.objects.get(id=myid)
    member.delete()
    members = Members.objects.all()
    return render(request, 'members.html', {'members' : members })


# TRANSACTIONS

def transactions(request):
    context = {}
    return render(request, 'transactions.html', context)
    
def services(request):
    context = {}
    return render(request, 'services.html', context)

def issuebook(request):
    context = {}
    return render(request, 'issuebook.html', context)

def issuebookreturn(request):
    context = {}
    return render(request, 'issuebookreturn.html', context)

def chargerentbookreturn(request):
    context = {}
    return render(request, 'chargerent.html', context)