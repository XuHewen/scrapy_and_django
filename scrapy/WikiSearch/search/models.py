from datetime import datetime

from django.db import models
from elasticsearch_dsl import (Boolean, Completion, Date, DocType, Keyword,
                               Nested, Text, analyzer)
from elasticsearch_dsl.connections import connections

connections.create_connection(hosts=['localhost'])


class WikiType(DocType):
    title = Text()
    url = Keyword()
    content = Text()

    class Meta:
        index = 'wiki'
        doc_type = 'article'


if __name__ == '__main__':
    WikiType.init()

# Create your models here.
