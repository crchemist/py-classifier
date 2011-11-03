import sys
import json
import urllib.request
import urllib.parse

class ClassifierKeyError(Exception):
    """This exception occurs when there is some issues with obtaining the key.
    """
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class ClassifierTrainError(Exception):
    """This exception occurs when there is some issues with train.
    """
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class ClassifierClassifyError(Exception):
    """This exception occurs when there is some issues with classify.
    """
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


class AntipClassifier(object):

    def __init__(self, host='api.antip.org.ua:80'):
        self.host = host

    def gen_new_key(self):
        url = 'http://{0}/key/'.format(self.host)
        try:
            response = urllib.request.urlopen(url, None)
        except urllib.request.URLError:
            raise ClassifierKeyError('Error occurs obtaining new key')
        data = json.loads(response.read().decode('utf-8'))
        return data.get("key")

    def set_key(self, key):
        self.key = key

    def train(self, data, category="porn"):
        params = urllib.parse.urlencode({'key': self.key, 'data': data, 'category': category})
        params = params.encode('utf-8')
        url = 'http://{0}/train/'.format(self.host)
        try:
            response = urllib.request.urlopen(url, params)
        except urllib.request.URLError:
            raise ClassifierTrainError('Error occurs while train: can\'t open url')
        else:
            data = json.loads(response.read().decode('utf-8'))
            if data.get("result") != "OK": return ClassifierTrainError(str(data))

    def classify(self, data):
        params = urllib.parse.urlencode({'key': self.key, 'data': data})
        params = params.encode('utf-8')
        url = 'http://{0}/classify/'.format(self.host)
        try:
            response = urllib.request.urlopen(url, params)
        except urllib.request.URLError:
            raise ClassifierTrainError('Error occurs while classify: can\'t open url')
        else:
            data = json.loads(response.read().decode('utf-8'))
            #if not  data.get("result"):
            #    raise ClassifierTrainError(str(data))
            return data

