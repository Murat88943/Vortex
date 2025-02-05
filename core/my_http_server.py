from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
from core.api import add_endpoint, handle_get, handle_post, handle_put, handle_delete, handle_patch, create_sample_endpoint, create_another_endpoint

# Настройка логирования
logging.basicConfig(level=logging.INFO)

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Обрабатываем GET-запрос"""
        logging.info(f"Received GET request for {self.path}")
        path = self.path
        handle_get(self, path)

    def do_POST(self):
        """Обрабатываем POST-запрос"""
        logging.info(f"Received POST request for {self.path}")
        path = self.path
        handle_post(self, path)

    def do_PUT(self):
        """Обрабатываем PUT-запрос"""
        logging.info(f"Received PUT request for {self.path}")
        path = self.path
        handle_put(self, path)

    def do_DELETE(self):
        """Обрабатываем DELETE-запрос"""
        logging.info(f"Received DELETE request for {self.path}")
        path = self.path
        handle_delete(self, path)

    def do_PATCH(self):
        """Обрабатываем PATCH-запрос"""
        logging.info(f"Received PATCH request for {self.path}")
        path = self.path
        handle_patch(self, path)

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    print("██╗   ██╗ ██████╗ ██████╗ ████████╗███████╗██╗  ██╗")
    print("██║   ██║██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝╚██╗██╔╝")
    print("██║   ██║██║   ██║██████╔╝   ██║   █████╗   ╚███╔╝ ")
    print("╚██╗ ██╔╝██║   ██║██╔══██╗   ██║   ██╔══╝   ██╔██╗ ")
    print(" ╚████╔╝ ╚██████╔╝██║  ██║   ██║   ███████╗██╔╝ ██╗")
    print("  ╚═══╝   ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝")

    # Регистрируем эндпоинты
    add_endpoint("/api/hello", create_sample_endpoint)
    add_endpoint("/api/another", create_another_endpoint)

    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    print("██╗   ██╗ ██████╗ ██████╗ ████████╗███████╗██╗  ██╗")
    print("██║   ██║██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝╚██╗██╔╝")
    print("██║   ██║██║   ██║██████╔╝   ██║   █████╗   ╚███╔╝ ")
    print("╚██╗ ██╔╝██║   ██║██╔══██╗   ██║   ██╔══╝   ██╔██╗ ")
    print(" ╚████╔╝ ╚██████╔╝██║  ██║   ██║   ███████╗██╔╝ ██╗")
    print("  ╚═══╝   ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝")
    run()
