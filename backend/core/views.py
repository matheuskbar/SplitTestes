from django.shortcuts import render
# from epub.reader import content


def index(request):
    # mybook = content.open_epub('meuEbook.epub')
    #
    # for item in mybook.opf.manifest.values():
    # # read the content
    # data = mybook.read_item(item)
    #
    # print(dir(mybook))
    return render(request, 'index.html')
