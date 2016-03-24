import urllib2, urllib
from BeautifulSoup import BeautifulSoup
from HTMLParser import HTMLParser
from django.utils.html import strip_tags
import xml.etree.ElementTree

def remove_tags(text):
    return ''.join(xml.etree.ElementTree.fromstring("<dummy_tag>" + text +"</dummy_tag>").itertext())

# class MLStripper(HTMLParser):
#     def __init__(self):
#         self.reset()
#         self.fed = []
#
#     def handle_data(self, d):
#         self.fed.append(d)
#
#     def get_data(self):
#         return ''.join(self.fed)


# def strip_tags(html):
#     s = MLStripper()
#     s.feed(html)
#     parser = HTMLParser()
#     html = parser.unescape(html)
#     return s.get_data()


base_url = 'https://wsearch.nlm.nih.gov/ws/query?db=healthTopics&term='
ret_type = '&rettype=brief'


def run_medline_query(search_terms):
    term = "{0}".format(search_terms)

    term = urllib.quote(term)


    results = []

    url = (base_url + term + ret_type)

    html = urllib.urlopen(url).read()


    soup = BeautifulSoup(html)




    for document in soup.findAll('document'):
        contents = document.findAll('content')
        for content in contents:
            if content.get('name') == 'title':
                taggedTitle = content.string
                title = strip_tags(taggedTitle)
            if content.get('name') == 'snippet':
                taggedSnippet = content.string
                snippet = strip_tags(taggedSnippet)
                snippet = strip_tags(snippet)
            if content.get('name') == 'FullSummary':
                taggedSummary = content.string
                summary = strip_tags(taggedSummary)
        print taggedTitle
        results.append({
            'title': remove_tags(title),
            'link': document.get('url'),
            'summary': remove_tags(snippet),
            'content': remove_tags(summary),
            'from': 'From:     MedlinePlus'
        })

    return results
