from datetime import datetime
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Date, Nested, Boolean, \
    analyzer, InnerObjectWrapper, Completion, Keyword, Text


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