Vortex

Это простой фреймворк на Python для создания HTTP-серверов и RESTful API. Он поддерживает основные HTTP методы (GET, POST, PUT, DELETE, PATCH), обработку ошибок, рендеринг шаблонов, а также поддержку CORS-заголовков.
Особенности

    Поддержка HTTP методов: GET, POST, PUT, DELETE, PATCH.
    Обработка ошибок с настраиваемыми сообщениями (400, 404, 422, 500).
    Поддержка CORS для кросс-доменных запросов.
    Рендеринг шаблонов с поддержкой Jinja-подобных шаблонов.
    Динамическая регистрация эндпоинтов.
    Ответы в формате JSON для удобной интеграции с API.

Установка

Для использования этого фреймворка вам нужно иметь установленный Python версии 3.7+.

    Клонируйте этот репозиторий:

Установите зависимости (если есть):

    pip install -r requirements.txt

    Убедитесь, что у вас есть папка templates/ в корневой директории для рендеринга HTML-шаблонов.

Использование
Запуск сервера

Для того чтобы запустить сервер, выполните файл main.py:

python main.py

Сервер будет запущен на порту 8080 по умолчанию. Вы можете изменить порт, изменив метод run() или передав другое значение порта в функцию run().
Создание и регистрация эндпоинтов

Фреймворк позволяет динамически регистрировать эндпоинты. Каждый эндпоинт связан с функцией-обработчиком, которая обрабатывает HTTP-запросы.

Пример регистрации эндпоинта:

from core.api import add_endpoint

def my_handler(self):
    data = {"message": "Hello, World!"}
    json_response(self, data)

add_endpoint("/api/hello", my_handler)

Вы можете зарегистрировать несколько эндпоинтов в функции register_endpoints(), которая вызывается в файле main.py.
Обработка ошибок

Фреймворк включает встроенные функции для обработки распространенных HTTP-ошибок, которые возвращают структурированные ответы в формате JSON. Вы можете использовать следующие методы для обработки ошибок:

    handle_400(self, message="Bad Request", error_data=None) — возвращает ошибку 400 (Bad Request).
    handle_404(self, message="Not Found", error_data=None) — возвращает ошибку 404 (Not Found).
    handle_422(self, message="Unprocessable Entity", error_data=None) — возвращает ошибку 422 (Unprocessable Entity).
    handle_500(self, message="Internal Server Error", error_data=None) — возвращает ошибку 500 (Internal Server Error).
    handle_200(self, message="OK", data=None) — возвращает успешный ответ с кодом 200.

Пример:

handle_400(self, "This is a bad request error!")

Эндпоинты
GET /

    Описание: Возвращает приветственное сообщение и список доступных эндпоинтов.
    Ответ:

    {
      "message": "Welcome to the API! Available endpoints: /api/get_json, /api/get_html, /api/post, /api/put, /api/delete, /api/patch"
    }

GET /api/get_json

    Описание: Возвращает JSON-ответ.
    Ответ:

    {
      "message": "This is a GET response in JSON format",
      "status": "success"
    }

GET /api/get_html

    Описание: Рендерит HTML-страницу с использованием шаблона test_template.html.
    Ответ: Рендерит простую HTML-страницу.

POST /api/post

    Описание: Принимает JSON-данные и возвращает их с добавленным полем "status".
    Запрос:

{
  "name": "John Doe"
}

Ответ:

    {
      "name": "John Doe",
      "status": "received"
    }

PUT /api/put

    Описание: Принимает JSON-данные и обновляет данные.
    Запрос:

{
  "name": "Jane Doe"
}

Ответ:

    {
      "message": "Updated data with PUT",
      "received_data": {
        "name": "Jane Doe"
      }
    }

DELETE /api/delete

    Описание: Удаляет данные и возвращает сообщение об успехе.
    Ответ:

    {
      "message": "Data has been deleted successfully",
      "status": "success"
    }

PATCH /api/patch

    Описание: Принимает JSON-данные и выполняет частичное обновление данных.
    Запрос:

{
  "name": "Doe"
}

Ответ:

    {
      "message": "Partially updated data",
      "patch_data": {
        "name": "Doe"
      }
    }

Тестирование ошибок

Вы можете протестировать различные HTTP ошибки с помощью следующих эндпоинтов:

    GET /api/test_error/400 — Возвращает ошибку 400 (Bad Request).
    GET /api/test_error/404 — Возвращает ошибку 404 (Not Found).
    GET /api/test_error/422 — Возвращает ошибку 422 (Unprocessable Entity).
    GET /api/test_error/500 — Возвращает ошибку 500 (Internal Server Error).
    GET /api/test_error/200 — Возвращает успешный ответ 200 (OK).

Рендеринг шаблонов

Фреймворк позволяет рендерить HTML-шаблоны с динамическими данными. Вот пример:

def handle_get_html(self):
    context = {
        "title": "Test Page",
        "message": "Welcome to the HTML page!"
    }
    render_template(self, "test_template.html", context)

Убедитесь, что файл test_template.html существует в папке templates/.

Пример содержимого шаблона test_template.html:

<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ message }}</h1>
</body>
</html>

CORS Поддержка

Фреймворк включает CORS-заголовки по умолчанию. Это позволяет использовать API с разных доменов.
Сотрудничество

Мы приветствуем ваши предложения и улучшения! Чтобы внести изменения, создайте форк репозитория, внесите изменения и создайте pull request.

При отправке pull request'ов, пожалуйста, убедитесь, что:

    Ваш код хорошо документирован.
    Вы написали тесты для нового функционала.
    Вы следуете стилю кода PEP 8.
