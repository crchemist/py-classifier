"""Classifies web pages depending on their title.
"""
import argparse
import urllib.request
import re
from classifier import AntipClassifier


HTML_TITLE_REGEXP = re.compile('<title>(?P<title>.+?)</title>')

def main():
    parser = argparse.ArgumentParser(description='Train antip classificator')
    parser.add_argument('-d', '--domains', dest='domains', required=True, help='path to file with domains list')
    parser.add_argument('-k', '--key', dest='key', required=True, help='key for cassifier ')
    args = parser.parse_args()
    domains = args.domains
    key = args.key
    
    train = AntipClassifier('api.antip.org.ua:80')
    train.set_key(key)

    for d in open(domains):
        d = d.strip()
        url='http://{0}/'.format(d)
        #print (d, url)
        try: 
            data = urllib.request.urlopen(url)
        except (urllib.request.URLError, UnicodeEncodeError) :
            print("can't open domain %s with url %s" %(d, url))
        else:
            try:
                data = data.read().decode('utf-8')
            except UnicodeDecodeError:
                print("can't open domain %s with url %s, problem with decode " %(d, url))
            else:
                title_match = HTML_TITLE_REGEXP.search(data)
                if title_match :
                    title = title_match.groupdict()['title']
                    print ('%s with title %s' %(d, title))
                    #train.train(title, 'porn')
                else:
                    print ('can not find title for domain %s' %d)
if __name__ == '__main__':
    main()
  

