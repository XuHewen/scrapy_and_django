from datetime import datetime

from elasticsearch_dsl import (Boolean, Completion, Date, DocType, Keyword,
                               Nested, Text, analyzer)
from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalyzer
from elasticsearch_dsl.connections import connections


class CustomAnalyzer(_CustomAnalyzer):
    def get_analysis_definition(self):
        return {}


connections.create_connection(hosts=['localhost'])

analyzer = CustomAnalyzer("standard")


class WikiType(DocType):
    suggest = Completion(analyzer=analyzer)
    title = Text()
    url = Keyword()
    content = Text()

    class Meta:
        index = 'wiki'
        doc_type = 'article'


if __name__ == '__main__':
    WikiType.init()
