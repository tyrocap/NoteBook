from django.urls import path
from .views import BookListView, NoteAddPage, Book_Add_Page, search_new_book,\
    note_add_book, add_new_book

urlpatterns = [
    path('', BookListView.as_view(), name='home_page'),
    path('notes/<uuid:pk>', NoteAddPage.as_view(), name='notes_page'),
    path('book/addition/', Book_Add_Page.as_view(), name='book_add_page'),
    path('search_book/', search_new_book, name='search_new_book'),
    path('note_add_book/', note_add_book, name='note_add_book'),
    path('add_new_book/', add_new_book, name='add_new_book'),
]