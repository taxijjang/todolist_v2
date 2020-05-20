import json
from urllib.request import urlopen

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView,FormView

from .models import DoTitle,DoComment

# home 화면 #

def get_api():
    dotitle_api_url = "http://127.0.0.1:8000/dotitle/"

    dotitle_source = urlopen(dotitle_api_url)

    dotitle_jsons = json.load(dotitle_source)

    DoTitle.objects.all().delete()

    for do in dotitle_jsons:
        dotitle = DoTitle(api_id = do['id'] , title = do['title'], body = do['body'], pub_date = do['pub_date'])
        dotitle.save()
        for cmt in do['docomment']:
            com = DoComment(title= dotitle, comment=cmt['comment'])
            com.save()

        print(do)


class DoTitleView(TemplateView):
    template_name = 'todolist/home.html'

    def get_context_data(self, **kwargs):
        print("@@ get_context_data @@")
        get_api()
        context = super().get_context_data(**kwargs)
        context['dotitles'] = DoTitle.objects.all()
        return context

class DoTitleDetail(DetailView):
    model = DoTitle
    template_name = 'todolist/detail.html'
    context_object_name = "dotitle"

