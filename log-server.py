# Records one JSON line per landed piece to play-log.jsonl, for tuning the speed equation.
from http.server import BaseHTTPRequestHandler, HTTPServer

class Log(BaseHTTPRequestHandler):
    def do_POST(self):
        body = self.rfile.read(int(self.headers['Content-Length']))
        with open('play-log.jsonl', 'ab') as f:
            f.write(body + b'\n')
        self.send_response(204)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def log_message(self, *args):
        pass

HTTPServer(('127.0.0.1', 8765), Log).serve_forever()
