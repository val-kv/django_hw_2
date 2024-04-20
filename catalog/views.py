from django.shortcuts import render
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from .forms import FeedbackForm


# Create your views here.
class HomePageView(View):
    def get(self, request):
        return render(request, 'home.html')


class ContactView(View):
    def get(self, request):
        form = FeedbackForm()
        return render(request, 'contact.html', {'form': form})

    def post(self, request):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Обработка данных формы (например, сохранение в базу данных)
            return HttpResponse('Thank you for your feedback!')
        return render(request, 'contact.html', {'form': form})

def home(request):
    return None


def contact(request):
    return None
