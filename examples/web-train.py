"""Classifies web pages depending on their title.
"""
import argparse
import urllib.request
import re
from classifier import AntipClassifier
import http

HTML_TITLE_REGEXP = re.compile('<title>(?P<title>.+?)</title>', re.I)
HTML_CHARSET_REGEXP = re.compile('Content-Type.*[encoding|charset]+=([a-zA-Z0-9-_]+)', re.I)
HTML_CHARSET_REGEXP_FROM_BODY = re.compile('charset=([a-zA-Z0-9-_]+)', re.I)

def main():
    parser = argparse.ArgumentParser(description='Train antip classificator')
    parser.add_argument('-d', '--domains', dest='domains', required=True, help='path to file with domains list')
    parser.add_argument('-k', '--key', dest='key', required=True, help='key for cassifier ')
    parser.add_argument('-c', '--category', dest='category', required=True, help='category name for cassifier ')
    args = parser.parse_args()
    domains = args.domains
    key = args.key
    category = args.category
    
    train = AntipClassifier('api.antip.org.ua:80')
    train.set_key(key)

    for d in open(domains):
        d = d.strip()
        charset_match = None
        url='http://{0}/'.format(d)
        try: 
            data = urllib.request.urlopen(url)  
        except (urllib.request.URLError, UnicodeEncodeError, http.client.BadStatusLine) :
            print("can't open domain %s with url %s" %(d, url))
            continue
        ### determine charset for domains - 1st: with http headers, 2nd:  from html body 
        data_read = data.read()
        try:
            headers = str(data.info())
        except:
            fuck = 1 
        else:
            charset_match = HTML_CHARSET_REGEXP.search(headers)
        if charset_match:
            charset = charset_match.group(1)
        else:
            charset_match = HTML_CHARSET_REGEXP_FROM_BODY.search(str(data_read))
            if charset_match:
                charset = charset_match.group(1)
            else:
                ### try to set utf-8 encode /// 
                charset='utf-8'
        if charset == 'win-1251':
            charset = 'windows-1251'
    
        try:
            data = data_read.decode(charset)
        except (UnicodeDecodeError, LookupError):
            print("can't open domain %s with url %s, problem with decode " %(d, url))
            continue
        title_match = HTML_TITLE_REGEXP.search(data)
        if title_match :
            title = title_match.groupdict()['title']
            print ('%s with title %s in: %s' %(d, title, category))
            train.train(title, category)
        else:
            print ('can not find title for domain %s' %d)
if __name__ == '__main__':
    main()
  

