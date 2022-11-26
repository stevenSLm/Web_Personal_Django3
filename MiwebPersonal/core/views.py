from django.shortcuts import render,HttpResponse

variable_base="""
<h1>MI WEB PERSONAL</H1>
       <ul>
            <li><a href="/">portada</a></li>
            <li><a href="/about/">acerca de...</a></li>
            <li><a href="/portfolio/">portafolio</a></li>
            <li><a href="/contact/">contacto del grupo...</a></li>
       </ul>
"""

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")


def contact(request):
    return  render(request, "core/contacto.html")     
