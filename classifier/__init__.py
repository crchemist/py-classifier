import sys
import json
import urllib.request

#from classifier import AntipClassifier
#classifier = AntipClassifier('xxx.xxx.xxx.xxx') # тобто айпішку вказати
#key = classifier.gen_new_key() # то перший раз коли ше ніякого ключа нема
#classifier.set_key(key)
#classifier.train(data="adsfasd", basket="spam")
#basket = classifier.classify('dasfaf')

class AntipClassifier(object):

    def __init__(self, host='api.antip.org.ua'):
        self.host = host
        print (host)

    def gen_new_key(self):
        print("generate new key")
        url = 'http://'+self.host+':9900/key/new'
        try:
            response = urllib.request.urlopen(url, None)
        except urllib.request.URLError:
            print("Can't open url", url, "... exit")
            sys.exit(1)
        # "key":"4bdb5c0d-b98a-4532-a129-cf2ed58ed40f"}
        data = json.loads(response.read().decode('utf-8'))
        #print("key=" ,key["key"])
        return data["key"] if "key" in data else None
    
    def set_key(self, key):
        self.key = key
    
    def train(self, data, basket="spam"):
        i=1


    

t = AntipClassifier('127.0.0.1')
key = t.gen_new_key()
print("end key=" ,key)
