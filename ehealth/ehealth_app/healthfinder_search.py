import urllib2, urllib
import json

healthfinder_api_key = "tfspmuwhxnezoirf"

base_url = "http://healthfinder.gov/developer/Search.json?"

def run_healthfinder_query(search_terms):
	keyword = "{0}".format(search_terms)
	keyword = urllib.quote(keyword)
	
	results = []
	
	url= (base_url + "api_key=" + healthfinder_api_key + "&keyword=" + keyword)
	
	response = urllib2.urlopen(url).read()
	json_response = json.loads(response)
	
	
	if json_response['Result'].has_key('Topics'):
		for result in json_response['Result']['Topics']:
				results.append({
				'title': result['Title'],
				'link': result['AccessibleVersion'],
				'from': "From:     Healthfinder.gov",
				'summary': result['Sections'][0]['Description'],
				'content': result['Sections'][0]['Content']
				})
			
		
	return results