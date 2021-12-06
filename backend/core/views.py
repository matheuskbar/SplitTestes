import html as html
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import TemplateView

import ebooklib
from ebooklib import epub
from ebooklib.epub import EpubBook


class IndexView(TemplateView):
    book = epub.read_epub('core/meuEbook.epub')
    template_name = 'index.html'
    #template_name = 'OEBPS/' + str(book.items[1].file_name)
    print(dir(book.items[0]))
    print('----------------------')
    print('----------------------')
    teste = book.items[0].get_body_content()

    s = '<html><head></head><body><h1>This is python</h1></body></html>'
    # Using html.escape() method
    gfg = html.escape(s)

    print(gfg)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['b'] = self.book
        context['items'] = self.book.items
        context['content'] = self.html
        return context


def book(request, int=0):
    book = epub.read_epub('core/meuEbook.epub')
    list = []
    for item in book.items:
        if item != book.items[-1] and item != book.items[-2]:
            list.append(item.file_name)
    pages = Paginator(list, 1)
    context = {
        'pages': pages
    }

    if int == 0:
        return render(request, 'OEBPS/' + str(list[int]), context)
    elif int == 1:
        return render(request, 'OEBPS/' + str(list[int]), context)
    elif int == 2:
        return render(request, 'OEBPS/' + str(list[int]), context)
    elif int == 3:
        return render(request, 'OEBPS/' + str(list[int]), context)
    elif int == 4:
        return render(request, 'OEBPS/' + str(list[int]), context)
