from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Book, Category


class BookDetail(DetailView):
    queryset = Book.objects.all()


class BookList(ListView):
    category = None
    paginate_by = 9

    def get_queryset(self):
        queryset = Book.objects.all()
        category_slug = self.kwargs.get('slug')

        if category_slug:
            self.category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=self.category)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        context["categories"] = Category.objects.all()
        return context
