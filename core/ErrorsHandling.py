import json

# Функция для установки CORS заголовков
def set_cors_headers(self):
    self.send_header('Access-Control-Allow-Origin', '*')
    self.send_header('Access-Control-Allow-Headers', 'Content-Type')
    self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, PATCH')

# Функция для отправки кастомных ошибок
def handle_error(self, code, message, error_data=None):
    """Обработка ошибок с кастомными сообщениями"""
    self.send_response(code)
    self.send_header('Content-type', 'application/json')
    set_cors_headers(self)
    self.end_headers()
    error_response = {"error": message}
    if error_data:
        error_response["details"] = error_data
    self.wfile.write(json.dumps(error_response, ensure_ascii=False).encode())

# Функция для обработки 400 ошибки (Bad Request)
def handle_400(self, message="Bad Request", error_data=None):
    handle_error(self, 400, message, error_data)

# Функция для обработки 404 ошибки (Not Found)
def handle_404(self, message="Not Found", error_data=None):
    handle_error(self, 404, message, error_data)

# Функция для обработки 422 ошибки (Unprocessable Entity)
def handle_422(self, message="Unprocessable Entity", error_data=None):
    handle_error(self, 422, message, error_data)

# Функция для обработки 500 ошибки (Internal Server Error)
def handle_500(self, message="Internal Server Error", error_data=None):
    handle_error(self, 500, message, error_data)

# Функция для обработки 200 (OK) ответа
def handle_200(self, message="OK", data=None):
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    set_cors_headers(self)
    self.end_headers()
    response = {"message": message}
    if data:
        response["data"] = data
    self.wfile.write(json.dumps(response, ensure_ascii=False).encode())
