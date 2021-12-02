from django.shortcuts import render
from django.views.generic import TemplateView

import ebooklib
from ebooklib import epub
from ebooklib.epub import EpubBook


class IndexView(TemplateView):
    template_name = "index.html"
    book = epub.read_epub('core/meuEbook.epub')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['b'] = self.book
        context['items'] = self.book.items
        return context


# def index(request):
#     book = epub.read_epub('core/meuEbook.epub')
#     print(dir(book))
#     return render(request, 'index.html', {'b': book})
