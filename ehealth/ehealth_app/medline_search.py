import urllib2, urllib

base_url= 'https://wsearch.nlm.nih.gov/ws/query?db=healthTopics&term='


def run_medline_query(search_terms):
	term = "{0}".format(search_terms)
	term = urllib.quote(term)
	
	results = []
	
	url= (base_url + term)
	
	response = urllib2.urlopen(url).read()
	
	
	
	for result in response['nlmSearchResult']['document']:
			results.append({
			'title': result['content']['title'],
			'link': result['url'],
			'from': "From:     Medline",
			'summary': result['content']['snippet']
			})
			
		
	return results