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
	document = dom.getElementsByTagName('document')
	
	for object in document:
		health_topic = object.getElementsByTagName('health-topic')
		for result in health_topic:
			summaries = result.getElementsByTagName('full-summary')
			results.append({
			'title': result.getAttribute('title'),
			'link': result.getAttribute('url'),
			'from': "From:     Medline Plus",
			'summary': " "
			})
			##for summary in summaries:
				##print summary.getElementsByTagName('p')
			
			
		
	return results