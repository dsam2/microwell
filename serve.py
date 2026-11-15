import http.server
import socket
import os
import sys

PORT = 3000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

REDIRECTS = {
    "/catalog.html": "/commercial-mattress-catalog.html",
    "/spec-sheets.html": "/commercial-mattress-spec-sheets.html",
    "/compliance.html": "/mattress-certifications-compliance.html",
    "/onboarding.html": "/wholesale-dealer-portal.html",
}

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        clean_path = self.path.split("?")[0]
        if clean_path in REDIRECTS:
            new_target = REDIRECTS[clean_path]
            query = self.path.split("?")[1] if "?" in self.path else ""
            if query:
                new_target += f"?{query}"
            self.send_response(301)
            self.send_header("Location", new_target)
            self.end_headers()
            return
        super().do_GET()

    def log_message(self, format, *args):
        sys.stderr.write(f"[{self.log_date_time_string()}] {format % args}\n")
        sys.stderr.flush()

def run():
    http.server.ThreadingHTTPServer.allow_reuse_address = True
    server_address = ("0.0.0.0", PORT)
    with http.server.ThreadingHTTPServer(server_address, Handler) as httpd:
        print(f"MICROWELL SERVER ACTIVE at:", flush=True)
        print(f"  --> http://localhost:{PORT}/", flush=True)
        print(f"  --> http://127.0.0.1:{PORT}/", flush=True)
        print(f"Serving directory: {DIRECTORY}", flush=True)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.", flush=True)

if __name__ == "__main__":
    run()
