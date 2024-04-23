from django.views import View
from django.http import HttpResponse
from .forms import FeedbackForm
from django.shortcuts import render


# Create your views here.
class HomePageView(View):
    def get(self, request):
        return render(request, 'main/home.html')


class ContactView(View):
    def get(self, request):
        form = FeedbackForm()
        return render(request, 'main/contact.html', {'form': form})

    def post(self, request):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Обработка данных формы (например, сохранение в базу данных)
            return HttpResponse('Thank you for your feedback!')
        return render(request, 'main/contact.html', {'form': form})


def home(request):
    return render(request, 'main/home.html')

def contact(request):
    return render(request, 'main/contact.html')
