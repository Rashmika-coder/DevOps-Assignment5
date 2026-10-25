from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SupermarketHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            response = {
                "status": "healthy",
                "application": "Supermarket Operations App"
            }
            self.send_response(200)
        elif self.path == "/":
            response = {
                "message": "Welcome to the Supermarket Operations App",
                "version": "1.0"
            }
            self.send_response(200)
        else:
            response = {"error": "Endpoint not found"}
            self.send_response(404)

        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 5000), SupermarketHandler)
    print("Supermarket application running on port 5000")
    server.serve_forever()
