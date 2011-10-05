import sys
import json
import urllib.request

#from classifier import AntipClassifier
#classifier = AntipClassifier('xxx.xxx.xxx.xxx') # тобто айпішку вказати
#key = classifier.gen_new_key() # то перший раз коли ше ніякого ключа нема
#classifier.set_key(key)
#classifier.train(data="adsfasd", basket="spam")
#basket = classifier.classify('dasfaf')

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
        print (host)

    def gen_new_key(self):
        print("generate new key")
        url = 'http://{0}/key/new'.format(self.host)
        try:
            response = urllib.request.urlopen(url, None)
        except urllib.request.URLError:
            #print("Can't open url", url, "... exit")
            raise ClassifierKeyError('Error occurs obtaining new key')
        data = json.loads(response.read().decode('utf-8'))
        return data.get("key")
    
    def set_key(self, key):
        self.key = key
    
    def train(self, data, basket="spam"):
        if not data :
            raise ClassifierTrainError('Error occurs while train: data argument missing')
        url = 'http://{0}/classifier/train?key={1}&text={2}&category={3}'.format(self.host, self.key, urllib.parse.quote(data), urllib.parse.quote(basket))
        try:
            response = urllib.request.urlopen(url, None)
        except urllib.request.URLError:
            raise ClassifierTrainError('Error occurs while train: can\'t open url')
        else:
            data = json.loads(response.read().decode('utf-8'))
            if data.get("result") != "OK": return ClassifierTrainError('Error occurs while train')
  
    def classify(self, data):
        if not data :
            raise ClassifierClassifyError('Error occurs while clasify: data argument missing')
        url = 'http://{0}/classifier/classify?key={1}&text={2}'.format(self.host, self.key, urllib.parse.quote(data))
        try:
            response = urllib.request.urlopen(url, None)
        except urllib.request.URLError:
            raise ClassifierTrainError('Error occurs while classify: can\'t open url')
        else:
            data = json.loads(response.read().decode('utf-8'))
            return data.get("result")


t = AntipClassifier('127.0.0.1:9900')
#key = t.gen_new_key()
key='1e3df71e-4f49-47f5-a163-3995a330fa47'
t.set_key(key)
#print("end key=" ,key)
#t.train('it is spam')
#t.train('this is not spam.. it good message', 'nonspam')
#t.train('')
#print (t.classify('it is spam'))
#raise ClassifierKeyError("test error")

