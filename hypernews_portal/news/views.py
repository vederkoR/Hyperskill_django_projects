from django.http import Http404
from django.shortcuts import render
from django.views import View
import json
from django.conf import settings


# Create your views here.


def index(request):
    return render(request, 'index.html')


class NewsView(View):
    def get(self, request, link, *args, **kwargs):
        with open(settings.NEWS_JSON_PATH) as json_file:
            news_article = json.load(json_file)
        articles = [article for article in news_article if article['link'] == link]
        if not articles:
            raise Http404("Resource not found")
        article = articles[0]
        return render(request, 'news_template.html', context={'news_article': article})
