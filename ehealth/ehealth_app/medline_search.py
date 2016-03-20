import urllib2, urllib
from xml.dom import minidom

base_url= 'https://wsearch.nlm.nih.gov/ws/query?db=healthTopics&term='
ret_type = '&rettype=topic'

					
def run_medline_query(search_terms):
	term = "{0}".format(search_terms)
	term = urllib.quote(term)
	
	results = []
	
	url= (base_url + term + ret_type)
	
	dom = minidom.parse(urllib.urlopen(url)) 
	
	for result in dom.getElementsByTagName('document'):
			print result.getAttribute('rank')
			results.append({
			'title': result.getAttribute('rank'),  ##placeholder until I can figure out how to access title
			'link': result.getAttribute('url'),
			'from': "From:     Medline Plus",
			'summary': 'content'  ## placeholder until I can access summary
			})
			
			
		
	return results