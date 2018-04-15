from http.server import HTTPServer, BaseHTTPRequestHandler
from jinja2 import Template
from database import Database

import simplejson

db = Database()

class HttpProcessor(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()

    def _create_html(self):
        file = open('static/index.html', 'r')
        template = Template(file.read())
        records = db.get_records()
        self.wfile.write(template.render(records=records).encode('utf-8'))

    def do_GET(self):
        self._set_headers()
        self._create_html()

    def do_POST(self):
        self._set_headers()

        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        data = simplejson.loads(self.data_string)

        db.add_record(data['login'], data['password'], data['text'])

        self._create_html()





serv = HTTPServer(("localhost",80), HttpProcessor)
serv.serve_forever()
