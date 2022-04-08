from django.shortcuts import render


def index(request):
    return render(request, 'my_journal_p/index.html')
# Create your views here.
