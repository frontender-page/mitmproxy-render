# Базовый образ с Python
FROM python:3.10-slim

# Устанавливаем mitmproxy
RUN pip install mitmproxy

# Создаем рабочую директорию
WORKDIR /app

# Копируем аддон в контейнер
COPY addon.py /app/addon.py

# Открываем порт для прокси
EXPOSE 8080

# Запускаем mitmdump с аддоном
CMD ["mitmdump", "-p", "8080", "-s", "/app/addon.py", "--set", "confdir=/app/.mitmproxy"]