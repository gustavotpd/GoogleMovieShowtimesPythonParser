import httplib, urllib, BeautifulSoup
from copy import deepcopy
from BeautifulSoup import BeautifulSoup

class GoogleMovieShowtimes:
	base_path = 'movies.google.com'

	def __init__(self, near, mid, tid):
		self.params = {'near': near, 'mid': mid, 'tid': tid}

		params = deepcopy(self.params)
		for key, val in params.iteritems():
			if val == '':
				self.params.pop(key)
		params = urllib.urlencode(self.params)

		'''conn = httplib.HTTPConnection(self.base_path)'''
		conn = httplib.HTTPConnection('www.google.com')
		print params
		conn.request("POST", "/movies", params)

		response = conn.getresponse()
		self.response_code = response.status
		self.response = response.getheaders
		self.response_body = response.read()

		if (self.response_code == 200):
			self.html = BeautifulSoup(self.response_body)

		print self.html.prettify()

	def check(self):
		if (self.response_code == 200):
			return True
		return False

