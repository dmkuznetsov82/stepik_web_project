#from cgi import parse_qs, escape
from urlparse import parse_qs

def wsgi_application(environ, start_response):
	# бизнес-логика
	status = '200 OK'
	headers = [
		('Content-Type', 'text/plain')
	]

	#params = parse_qs(environ['QUERY_STRING'])
	
	#body = ''
	#for k in sorted(params.iterkeys()):
	#	body += k + "=".join(params[k]) + "\r\n"

	body = [bytes(i + '\r\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]

	start_response(status, headers)
	return body 
