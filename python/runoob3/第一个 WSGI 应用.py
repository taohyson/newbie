def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]

$ uwsgi --http :9090 --wsgi-file 第一个WSGI应用.py