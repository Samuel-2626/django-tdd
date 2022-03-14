from django.shortcuts import render

from .forms import AddCatalogueForm

def home(request):

    add_catalogue_form = AddCatalogueForm()

    return render(request, 'home.html', {
        "add_catalogue_form": add_catalogue_form,
    })