from django.urls import path

from .views import BookList, BookDetail, BookCreateView

app_name = 'book'

urlpatterns = [
    path('', BookList.as_view(), name='list'),
    path("category/<slug:slug>/", BookList.as_view(), name="list_by_category"),
    path('<slug:slug>/', BookDetail.as_view(), name='detail'),
    path('new-book', BookCreateView.as_view(), name='new_book')
]
