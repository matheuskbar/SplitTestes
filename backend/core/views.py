from django.shortcuts import render
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import pink, black, red, blue, green


def index(request):
    c = Test('teste.pdf', pagesize=A4)
    c.setFont("Helvetica", 16)
    c.setFillColorRGB(1, 0, 1)
    c.drawString(100, 700, "Olá mundo!!")
    c.showPage()
    teste = f'testando aqui uma linha\n outra linha\ne outra\n e outra'
    text = c.beginText()
    text.setTextOrigin(inch, 10*inch)
    text.setFont("Helvetica-Oblique", 14)
    text.textLines('''Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    Proin in mollis nisl. Proin scelerisque neque sed dolor imperdiet dignissim. 
    Aenean pellentesque, massa eu varius dictum, erat diam elementum orci, nec ull
    amcorper enim sem nec orci. Donec rhoncus diam at elit luctus, nec placerat ju
    sto euismod. Suspendisse id justo convallis, venenatis lectus non, rhoncus orci
    . Suspendisse mollis risus arcu, vitae tincidunt metus dapibus sit amet. Nunc 
    mollis enim elit, consectetur consectetur mi elementum sed. Mauris pretium mi 
    magna, ut venenatis odio finibus eget. Sed gravida sodales mollis. Ut venenati
    s, neque a venenatis imperdiet, erat leo hendrerit eros, sit amet lobortis mau
    ris erat eu velit. Nullam ullamcorper sem nec ultrices porta. Sed feugiat eget 
    urna eget egestas. Quisque accumsan iaculis mauris, et consectetur ligula elei
    fend sed. Cras lacinia nec mi vel iaculis. Nam vel quam nisl.

    Praesent sit amet purus sit amet orci sagittis iaculis. Donec non ipsum non n
    eque dignissim congue. Sed vel lorem vel metus aliquet iaculis eu quis ante. 
    In scelerisque ullamcorper enim eget efficitur. Curabitur pulvinar laoreet au
    ctor. Donec enim ante, malesuada sit amet laoreet porttitor, sollicitudin ege
    t leo. Suspendisse purus libero, dictum non arcu sit amet, blandit vehicula m
    agna. Integer vel accumsan velit. Sed iaculis, libero vitae fermentum egestas
    , felis est semper eros, eget cursus dui ex vulputate ipsum. Pellentesque vul
    putate, orci sed consequat euismod, quam enim vehicula sapien, vel facilisis 
    tellus dolor gravida orci. Fusce faucibus ante in neque congue, quis fermentu
    m neque imperdiet. Mauris orci magna, convallis sed laoreet sed, egestas ut a
    nte. Nunc cursus mauris aliquet vehicula tempor. Sed accumsan neque vitae veh
    icula tincidunt.'''
                   )
    c.drawText(text)

    c.save()

    return render(request, 'index.html', {'c': c})


class Test(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
