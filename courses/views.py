from django.shortcuts import render

from .models import News
from .forms import RecordForm


def main(request):
    items = News.objects.all()
    context = {'items': items}
    return render(request, 'main.html', context)


def register(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'register.html', {'info': 'Вы были успешно добавлены.'})
        else:
            return render(request, 'register.html', {'form': form})
    else:
        return render(request, 'register.html')


def about(request):
    return render(request, 'about.html')