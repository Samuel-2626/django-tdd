from django.shortcuts import render

from .forms import AddCatalogueForm

from .models import Catalogue

def home(request):

    
    # Save a new book to the catalogue
    if request.method == 'POST':

        add_catalogue_form = AddCatalogueForm(data=request.POST)

        # cheeck if the form is valid
        if add_catalogue_form.is_valid():
            add_catalogue_form.save()

    # Get all books from the catalogue
    books = Catalogue.objects.all()

    # Show the empty form for users to fill
    add_catalogue_form = AddCatalogueForm()   


    return render(request, 'home.html', {
        "add_catalogue_form": add_catalogue_form,
        "books": books
    })