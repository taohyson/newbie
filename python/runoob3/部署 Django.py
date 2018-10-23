def application(env, start_response):
	start_response('200 OK', [('Content-Type','text/html')])
	return [b"Hello python"]

$ vim 部署Django.ini
[uwsgi]
socket = 0.0.0.0:9090
wsgi-file = 部署Django.py
processes = 4
threads = 2
stats = 0.0.0.0:9091
$ uwsgi 部署Django.ini