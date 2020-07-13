import elasticsearch

class FooService:

    def __init__(self):
        self.es = elasticsearch.Elasticsearch(hosts=[{'host': 'localhost', 'port': 9200}])

    def create(self, index, body):
        es_object = self.es.index(index, body)
        return es_object.get('_id')

    def read(self, index, id):
        es_object = self.es.get(index, id)
        return es_object.get('_source')
