from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Book, CustomUser, Note
from django.contrib.postgres.search import SearchVector
import os
import xml.etree.ElementTree as ET
import requests
from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
import json
from django.http import HttpResponse
from django.views.generic.detail import DetailView

class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'
    paginate_by = 2
    template_name = 'home-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.GET.get('contains_qs'):
            context['filtered_book_list'] = Book.objects.annotate(
                search=SearchVector(
                    'title', 'author', 'category'), ).filter(
                search=self.request.GET.get(
                    'contains_qs'))
            return context
        elif self.request.GET.get('qrall'):
            return context
        elif self.request.GET.get('qrbus'):
            context['filtered_book_list'] = Book.objects.filter(
                category='business')
            return context
        elif self.request.GET.get('qrinv'):
            context['filtered_book_list'] = Book.objects.filter(
                category='investing')
            return context
        elif self.request.GET.get('qrbio'):
            context['filtered_book_list'] = Book.objects.filter(
                category='biography')
            return context
        else:
            return context


    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('notes_page', args=[str(self.id)])


class NoteAddPage(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'notes-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_notes'] = Note.objects.filter(
            note_user=self.request.user, note_book=self.object)
        return context

def note_add_book(request):
    if request.method == 'POST':
        print(request.body)
        data = json.loads(request.body)

        # user of the note
        note_user = request.user

        # book related to note
        comment_book_id = data['note_book_id123']
        note_book = Book.objects.get(id=comment_book_id)

        # text of the note
        note_body = comment_text = data['note_book_textarea']

        note = Note(note_user=note_user, note_book=note_book,
                    note_body=note_body)
        note.save()

        response_data = {}
        response_data['comment_text'] = comment_text

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )

    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

class Book_Add_Page(ListView):
    model = CustomUser
    context_object_name = 'cuser'
    template_name = 'book-add-page.html'


def search_new_book(request):
    if request.method == 'GET':
        title = request.GET.get('add_book_goodreads')

        # API call to get book info (GOODREADS)
        book_id_search_url = 'https://www.goodreads.com/search/index.xml'
        params_id_search = {
            "q": title,
            "key": os.environ.get('GOODREADS_KEY'),
            "search": 'all',
        }
        content_id_search = requests.get(url=book_id_search_url,
                                         params=params_id_search)
        root_id_search = ET.fromstring(content_id_search.text)

        # DESIRED API RESULSTS
        title_goodreads = root_id_search[1][6][0][8][1].text
        author_goodreads = root_id_search[1][6][0][8][2].text
        image_url_goodreads = root_id_search[1][6][0][8][3].text
        book_id_search = root_id_search[1][6][0][8][0].text


        # API call to get book info (GOOGLE)
        api_key_google = os.environ.get('GOOGLE_API_KEY')
        book_url_google = f'https://www.googleapis.com/books/v1/volumes?q=intitle:{title}&key={api_key_google}'
        content_google = requests.get(url=book_url_google).json()

        # DESIRED API RESULSTS
        title_google = content_google['items'][0]['volumeInfo']['title']
        author_google = content_google['items'][0]['volumeInfo']['authors'][0]
        image_url_google = content_google['items'][0]['volumeInfo']['imageLinks']['smallThumbnail']

        context = {
                'title_goodreads': title_goodreads,
                'author_goodreads': author_goodreads,
                'image_url_goodreads': image_url_goodreads,
                'book_id_search': book_id_search,

                'title_google': title_google,
                'author_google': author_google,
                'image_url_google': image_url_google,
            }
    return render(request, template_name='search-results.html', context=context)

def add_new_book(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            # id THAT GOODREADS API CALL IS BASED UPON
            book_id_search = data['book_id_search']

            # GOODREADS # GOODREADS
            # GOODREADS # GOODREADS
            # GOODREADS # GOODREADS
            # API call to get book info (GOODREADS)
            book_info_get_url = 'https://www.goodreads.com/book/show.xml'
            params_info_get = {
                "key": os.environ.get('GOODREADS_KEY'),
                "id": book_id_search,
            }
            content_info_get = requests.get(url=book_info_get_url,
                                            params=params_info_get)
            root_info_get = ET.fromstring(content_info_get.text)

            # DESIRED API RESULSTS
            try:
                title_goodreads = root_info_get[1][1].text
            except:
                title_goodreads = ''
            try:
                author_goodreads = root_info_get[1][26][0][1].text
            except:
                author_goodreads = ''
            try:
                isbn13_goodreads = root_info_get[1][3].text
            except:
                isbn13_goodreads = 1
            try:
                description_goodreads = root_info_get[1][16].text
            except:
                description_goodreads = ''
            try:
                ratings_sum_count_book_goodreads = root_info_get[1][17][4].text
            except:
                ratings_sum_count_book_goodreads = 1
            try:
                average_rating_goodreads = root_info_get[1][18].text
            except:
                average_rating_goodreads = 1
            try:
                num_pages_goodreads = root_info_get[1][19].text
            except:
                num_pages_goodreads = 1
            try:
                image_url_goodreads = root_info_get[1][8].text
            except:
                image_url_goodreads = ''
            try:
                category_goodreads = (
                            root_info_get[1][28][0].attrib['name'] + ' ' +
                            root_info_get[1][28][1].attrib['name'] + ' ' +
                            root_info_get[1][28][2].attrib[
                                'name']).replace('to-read',
                                                 '').replace(
                    'currently-reading', '').rstrip().lstrip()
            except:
                category_goodreads = ''

            # Once the button is pressed, add the book to the database
            try:
                book = Book.objects.get(title=title_goodreads)
            except ObjectDoesNotExist:
                book = Book(
                    title=title_goodreads,
                    author=author_goodreads,
                    category=category_goodreads,
                    description=description_goodreads,
                    image=image_url_goodreads,
                    primary_isbn13=isbn13_goodreads,
                    page_count=num_pages_goodreads,
                    average_rating=average_rating_goodreads,
                    rating_count=ratings_sum_count_book_goodreads
                )
                book.save()
        except:
            messages.error(request, "There occured an unexpected error.")


        try:
            # title THAT GOOGLE API IS BASED UPON
            title_google = data['title_google']
            # GOOGLE # GOOGLE
            # GOOGLE # GOOGLE
            # GOOGLE # GOOGLE
            # API call to get book info (GOOGLE)
            api_key_google = os.environ.get('GOOGLE_API_KEY')
            book_url_google = f'https://www.googleapis.com/books/v1/volumes?q=intitle:{title_google}&key={api_key_google}'
            content_google = requests.get(url=book_url_google).json()

            # DESIRED API RESULSTS
            try:
                title_google = content_google['items'][0]['volumeInfo']['title']
            except:
                title_google = ''
            try:
                author_google = \
                    content_google['items'][0]['volumeInfo']['authors'][
                        0]
            except:
                author_google = ''
            try:
                image_url_google = \
                    content_google['items'][0]['volumeInfo']['imageLinks'][
                        'smallThumbnail']
            except:
                image_url_google = ''
            try:
                description_google = content_google['items'][0]['volumeInfo'][
                    'description']
            except:
                description_google = ''
            try:
                average_rating_google = \
                    content_google['items'][0]['volumeInfo'][
                        'averageRating']
            except:
                average_rating_google = 1
            try:
                rating_count_google = content_google['items'][0]['volumeInfo'][
                    'ratingsCount']
            except:
                rating_count_google = 1

            try:
                categories_google = \
                    content_google['items'][0]['volumeInfo']['categories'][0]
            except:
                categories_google = "None"
            try:
                isbn13_google = \
                    content_google['items'][0]['volumeInfo'][
                        'industryIdentifiers'][
                        0]['identifier']
            except:
                isbn13_google = 1
            try:
                num_pages_google = content_google['items'][0]['volumeInfo'][
                    'pageCount']
            except:
                num_pages_google = 1

            # Once the button is pressed, add the book to the database
            try:
                book = Book.objects.get(title=title_google)
            except ObjectDoesNotExist:
                book = Book(
                    title=title_google,
                    author=author_google,
                    category=categories_google,
                    description=description_google,
                    image=image_url_google,
                    primary_isbn13=isbn13_google,
                    page_count=num_pages_google,
                    average_rating=average_rating_google,
                    rating_count=rating_count_google
                )
                book.save()
        except:
            messages.error(request, "There occured an unexpected error.")

        print(request.body)
        print('A'*100)
    return HttpResponse('')











