from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book


class Another(View) :

    books = Book.objects.get(title="Harry Potter")
    book1 = Book.objects.filter(title="Harry Potter")
    for x in book1:
        name = x.title
    output = f"Book 1 =  {books.title} book2 = {name}"


    def get(self, request) :
        print(type(self.books))
        print(self.books)
        print(type(self.book1))
        print(self.book1)
        return HttpResponse(self.output)

def first(request) :
    return HttpResponse('First Message from views')
