Как сгенерировать ключ для доступа к API

## Шаг 1

Зарегистрировать новое мобильное приложение, получить уникальный id (client_id).

В настройках приложения указать адрес `http://127.0.0.1:5000` - "Адрес сайта" и "Redirect URI" .

## Шаг 2

Запустить flask

```bash
export FLASK_APP=server.py
export FLASK_ENV=development
export YMONEY_APP_ID=2F8CD5B641C014C261FAC1138D10297DE807B281CF580271A3391AF6BC2D8863 # подставить id своего приложения
flask run
```

Заходим на [127.0.0.1:5000](http://127.0.0.1), жмем на кнопку, получаем токен.

# Документация Яндекс Денег

[Как это работает](https://tech.yandex.ru/money/doc/dg/reference/request-access-token-docpage/)
