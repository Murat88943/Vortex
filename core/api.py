import json
import os
from urllib.parse import urlparse
from jinja2 import Environment, FileSystemLoader

# Словарь для хранения всех эндпоинтов
api_endpoints = {}

# Папка с HTML-шаблонами
TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), '../templates')

# Настройка Jinja2 для рендеринга шаблонов
env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

# Метод для добавления нового эндпоинта
def add_endpoint(path, handler):
    """Добавляет новый эндпоинт и его обработчик"""
    api_endpoints[path] = handler


# Метод для обработки ответа в формате JSON
def json_response(self, data, status_code=200):
    """Возвращает JSON-ответ с данным статусом"""
    self.send_response(status_code)
    self.send_header('Content-type', 'application/json')
    self.end_headers()
    self.wfile.write(json.dumps(data, ensure_ascii=False).encode())


# Метод для обработки ошибок
def json_error(self, message, status_code=400):
    """Возвращает ошибку в формате JSON"""
    self.send_response(status_code)
    self.send_header('Content-type', 'application/json')
    self.end_headers()
    error_data = {"error": message}
    self.wfile.write(json.dumps(error_data, ensure_ascii=False).encode())


# Рендеринг HTML-шаблонов с использованием Jinja2
def render_template(self, template_name, context={}):
    """Рендерит HTML-шаблон и отправляет клиенту"""
    try:
        # Получаем шаблон
        template = env.get_template(template_name)

        # Рендерим шаблон с контекстом
        html_content = template.render(context)

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html_content.encode())

    except Exception as e:
        json_error(self, str(e), 500)


# Пример стандартного обработчика GET-запросов для всех эндпоинтов
def handle_get(self, path):
    """Обрабатывает GET-запросы и передает управление соответствующему обработчику"""
    if path in api_endpoints:
        handler = api_endpoints[path]
        handler(self)
    else:
        json_error(self, "Endpoint not found", 404)


# Пример стандартного обработчика POST-запросов для всех эндпоинтов
def handle_post(self, path):
    """Обрабатывает POST-запросы и передает управление соответствующему обработчику"""
    if path in api_endpoints:
        handler = api_endpoints[path]
        handler(self)
    else:
        json_error(self, "Endpoint not found", 404)


# Пример стандартного обработчика PUT-запросов для всех эндпоинтов
def handle_put(self, path):
    """Обрабатывает PUT-запросы и передает управление соответствующему обработчику"""
    if path in api_endpoints:
        handler = api_endpoints[path]
        handler(self)
    else:
        json_error(self, "Endpoint not found", 404)


# Пример стандартного обработчика DELETE-запросов для всех эндпоинтов
def handle_delete(self, path):
    """Обрабатывает DELETE-запросы и передает управление соответствующему обработчику"""
    if path in api_endpoints:
        handler = api_endpoints[path]
        handler(self)
    else:
        json_error(self, "Endpoint not found", 404)


# Пример стандартного обработчика PATCH-запросов для всех эндпоинтов
def handle_patch(self, path):
    """Обрабатывает PATCH-запросы и передает управление соответствующему обработчику"""
    if path in api_endpoints:
        handler = api_endpoints[path]
        handler(self)
    else:
        json_error(self, "Endpoint not found", 404)


### --- ПРИМЕР ЭНДПОИНТОВ --- ###

# Пример создания простого эндпоинта для JSON-ответа
def create_sample_endpoint(self):
    """Пример обработчика для конкретного эндпоинта"""
    data = {
        "message": "Hello, World!",
        "status": "success"
    }
    json_response(self, data)


# Пример другого эндпоинта для JSON-ответа
def create_another_endpoint(self):
    """Другой обработчик для эндпоинта"""
    data = {
        "message": "Another endpoint response",
        "status": "success"
    }
    json_response(self, data)


# Пример эндпоинта для рендеринга HTML-шаблона
def render_html_endpoint(self):
    """Обработчик для рендеринга HTML-шаблона"""
    context = {
        "title": "My API Page",
        "message": "Welcome to the API-driven site!"
    }
    render_template(self, 'index.html', context)
