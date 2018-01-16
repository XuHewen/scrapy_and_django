# import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic.base import View
from elasticsearch import Elasticsearch

from .models import WikiType

client = Elasticsearch(hosts=['127.0.0.1'])


# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')


class suggestView(View):

    def get(self, request):
        key_words = request.GET.get('s', '')
        re_data = []
        if key_words:
            s = WikiType.search()
            s = s.suggest('my_suggest', key_words, completion={
                'field': 'suggest',
                'fuzzy': {
                    'fuzziness': 2
                }
            })
            suggestions = s.execute()
            for match in suggestions.suggest['my_suggest'][0].options:
                if match:
                    source = match._source
                    re_data.append(source['title'])

        # return HttpResponse(json.dumps(re_data), content_type='application/json')
        return JsonResponse(re_data, safe=False)


class SearchView(View):

    def get(self, request):
        key_words = request.GET.get('q', '')
        response = client.search(
            index='wiki',
            body={
                'query': {
                    'multi_match': {
                        'query': key_words,
                        'fields': ['title', 'content']
                    }
                },
                'from': 0,
                'size': 10,
                'highlight': {
                    'pre_tags': ['<span class="keyword">'],
                    'post_tags': ['</span>'],
                    'fields': {
                        'title': {},
                    }
                }
            }
        )

        total_nums = response['hits']['total']
        hit_list = []
        for hit in response['hits']['hits']:
            hit_dict = {}

            try:
                if 'title' in hit['highlight']:
                    hit_dict['title'] = hit['highlight']['title']
            except:
                hit_dict['title'] = hit['_source']['title']
            else:
                hit_dict['title'] = hit['_source']['title']


            hit_dict['content'] = hit['_source']['content'][:500]

            hit_dict['score'] = hit['_score']
            hit_dict['url'] = hit['_source']['url']
            hit_dict['created_date'] = '2018-01-01'

            hit_list.append(hit_dict)

        return render(request, 'result.html',
                      {'all_hits': hit_list, 'key_words': key_words})
