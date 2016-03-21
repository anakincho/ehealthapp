import urllib2, urllib
from xml.dom import minidom
from HTMLParser import HTMLParser


class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
	s = MLStripper()
	s.feed(html)
	parser = HTMLParser()
	html = parser.unescape(html)
	return s.get_data()


base_url= 'https://wsearch.nlm.nih.gov/ws/query?db=healthTopics&term='
ret_type = '&rettype=brief'

					
def run_medline_query(search_terms):
	term = "{0}".format(search_terms)
	term = urllib.quote(term)
	none = 'none'
	
	results = []
	
	url= (base_url + term + ret_type)
	
	dom = minidom.parse(urllib.urlopen(url)) 
	documents = dom.getElementsByTagName('document')
	
	for document in documents:
		contents = document.getElementsByTagName('content')
		for item in contents:
			actualContent = item.firstChild.nodeValue
			if item.getAttribute('name') == 'title':
				title = strip_tags(actualContent)
			if item.getAttribute('name') == 'snippet':
				summary = strip_tags(actualContent)
			if item.getAttribute('name') == 'FullSummary':
				content = strip_tags(actualContent)
		
		results.append({
		'title' : title,
		'link' : document.getAttribute('url'),
		'summary': summary,
		'content':  content,
		'from' : 'From:     MedlinePlus'
		})	
		
			
			
		
	return results