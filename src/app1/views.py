from django.shortcuts import render
from app1.forms import PhoneForm


def index(request):
    if request.method == 'POST':
        form = PhoneForm(request.POST)
        if form.is_valid():
            pass

    else:
        form = PhoneForm()

    return render(request, 'phonenumbers.html', {'form': form})
