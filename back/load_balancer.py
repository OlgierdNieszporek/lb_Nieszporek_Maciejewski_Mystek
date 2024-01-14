import http.server
import socketserver
import random


class LoadBalancerHandler(http.server.SimpleHTTPRequestHandler):
    backend_servers = [
        ('localhost', 5001),
        ('localhost', 5002),
        ('localhost', 5003),
        ('localhost', 5004)
    ]

    def do_GET(self):
        print('TEST')
        backend_server = random.choice(self.backend_servers)
        self.proxy_to(backend_server)

    def proxy_to(self, backend_server):
        self.send_response(302)
        self.send_header('Location', f'http://{backend_server[0]}:{backend_server[1]}{self.path}')
        self.end_headers()


if __name__ == '__main__':
    port = 8080
    with socketserver.TCPServer(("", port), LoadBalancerHandler) as httpd:
        print(f"Load balancer running on port {port}")
        httpd.serve_forever()
