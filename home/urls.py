from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("books", views.books, name='books'),
    path("members", views.members, name='members'),
    path("transactions", views.transactions, name='transcations'),
    path("services", views.services, name='services'),
    path("issuebook", views.issuebook, name='issuebook'),
    path("issuebookreturn", views.issuebookreturn, name='issuebookreturn'),
    path("chargerentbookreturn", views.chargerentbookreturn, name='chargerentbookreturn'),
    path("add_member", views.add_member, name='add_member'),
    path("delete_member/<int:myid>/", views.delete_member, name='delete_member'),
    path("add_book", views.add_book, name='add_book'),
    path("delete_book/<int:myid>/", views.delete_book, name='delete_book'),
]