from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import urlparse


class Palvelu(BaseHTTPRequestHandler):
    """ GET /tervehdys/Ahto """
    def do_GET(self):
        uri = urlparse.urlparse(self.path)
        path = uri.path.strip('/').split('/')

        if len(path) != 2 or path[0] != 'tervehdys':
            self.send_response(404)
            self.end_headers()
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Cache-Control', 'max-age=31536000')
            self.end_headers()
            nimi = path[1]
            tervehdys = "Moi %s!" % nimi
            self.wfile.write(tervehdys + "\n")
            self.wfile.close()
 

if __name__ == "__main__":
    httpd = HTTPServer(('', 8080), Palvelu)
    httpd.serve_forever()

