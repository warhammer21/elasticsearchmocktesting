import urllib.request
import json
service = 'localhost:9200/'
import base64

def basic_header(username, password):
    combined_bytes = (username + ':' + password).encode('utf-8')
    encoded_bytes = base64.b64encode(combined_bytes)
    return 'Basic ' + encoded_bytes.decode('ascii')

class ElasticClient:
    service = "https://localhost:9200/"
    def __init__(self,):
        self.headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        #'Authorization': ElasticClient.basic_header(api_key, password),
        }
    @staticmethod
    def basic_header(username, password=''):
        """
        >>> ElasticClient.basic_header('Aladdin', 'OpenSesame')
        'Basic QWxhZGRpbjpPcGVuU2VzYW1l'
        """
        combined_bytes = (username + ':' + password).encode('utf-8')
        encoded_bytes = base64.b64encode(combined_bytes)
        return 'Basic ' + encoded_bytes.decode('ascii')

    def load_eventlog(self, data_document):
        request = urllib.request.Request(
        url='http://localhost:9200/v0/eventlog' ,
        headers=self.headers,
        method='POST',
        data=json.dumps(data_document).encode('utf-8')
        )
        with urllib.request.urlopen(request) as response:
            assert response.status == 201, "Insertion Error"
            response_headers = dict(response.getheaders())
            return response_headers['Location']

