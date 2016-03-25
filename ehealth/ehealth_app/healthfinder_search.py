import urllib2
import urllib
import json

healthfinder_api_key = "tfspmuwhxnezoirf"

base_url = "http://healthfinder.gov/developer/Search.json?"


def run_healthfinder_query(search_terms):
    keyword = "{0}".format(search_terms)
    keyword = urllib.quote(keyword)

    results = []

    url = (base_url + "api_key=" + healthfinder_api_key + "&keyword=" + keyword)

    response = urllib2.urlopen(url)
    json_response = json.load(response)

    if json_response['Result'].has_key('Topics'):

        for result in json_response['Result']['Topics']:
            if 'Sections' not in result:
                continue
            try:
                results.append({
                    'title': result['Title'],
                    'link': result['AccessibleVersion'],
                    'from': "From:     Healthfinder.gov",
                    'summary': result['Sections'][0]['Description'],
                    'content': result['Sections'][0]['Content']
                })
            except TypeError:
                print "healthfinder API is a bad thing or there are no results"

    if len(results) == 0:
        print "no results, but have to rewrite the whole view in order to display a no results message on the website..."

    return results
