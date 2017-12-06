
from html.parser import HTMLParser
from urllib.parse import urlparse
from urllib.parse import urljoin



#by putting HTMLParser inside class
# we inherit all the functionality
class LinkFinder(HTMLParser):
	#class initialization
	def __init__(self, base_url, page_url):
		super().__init__()
		self.base_url = base_url
		self.page_url = page_url
		self.links = set()

	def handle_starttag(self,tag,attrs):
		#feed is returning the starting tags so 
		# we can check which tag we want to crwal by links
		if tag == 'a':
			for(attibure,value) in attrs:
				if attibure == 'href':
					#url = parse.urljoin(self.base_url,value)
					url = urljoin(self.base_url,value)
					self.links.add(url)
					#print(url)
					#print(links)

	def page_links(self):
		return self.links

	def error(self,message):
		pass



