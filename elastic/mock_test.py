import unittest
from unittest.mock import *
import doctest
from elastic_mock import ElasticClient
import json
class GIVEN_ElasticClient_WHEN_load_eventlog_THEN_request(unittest.TestCase):
    def setUp(self) -> None:

        self.mock_response = Mock()
        self.mock_response.status = 201
        self.mock_response.getheaders.return_value = {'Location': 'http://localhost:9200/v0/eventlog/_doc/1'}

        # The test document.
        self.data_document = {
            "timestamp": "2016-06-15T17:57:54.715",
            "levelname": "INFO",
            "module": "ch09_r10",
            "message": "Sample Message One"
        }
    @patch('elastic_mock.urllib.request.urlopen')
    def runTest(self,mock_urlopen):
        mock_urlopen.return_value.__enter__.return_value = self.mock_response

        client = ElasticClient()
        response_location = client.load_eventlog(self.data_document)
        # Assert that the response location is as expected
        self.assertEqual(response_location, 'http://localhost:9200/v0/eventlog/_doc/1')

        # Verify the request was made with correct parameters
        call_args = mock_urlopen.call_args[0][0]
        print(call_args)
        self.assertEqual(call_args.full_url, 'http://localhost:9200/v0/eventlog')
        self.assertEqual(call_args.method, 'POST')
        self.assertEqual(call_args.headers['Accept'], 'application/json')
        self.assertEqual(json.loads(call_args.data), self.data_document)


        # Ensure that urlopen was called once
        mock_urlopen.assert_called_once()


