from django.shortcuts import render
from django.views import View


class Main(View):

    @staticmethod
    def get(request):
        return render(request, 'index.html')
