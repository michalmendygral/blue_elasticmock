from unittest import TestCase
from elasticmock import elasticmock
from foo.bar import FooService

class FooServiceTest(TestCase):

    @elasticmock
    def test_should_create_and_read_object(self):
        # Variables used to test
        index = 'test-index'
        expected_document = {
            'foo': 'bar'
        }

        # Instantiate service
        service = FooService()

        # Index document on ElasticSearch
        id = service.create(index, expected_document)
        self.assertIsNotNone(id)

        # Retrive dpcument from ElasticSearch
        document = service.read(index, id)
        self.assertEquals(expected_document, document)
