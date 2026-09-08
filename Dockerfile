FROM python:3.10-slim

# Устанавливаем mitmproxy и Flask
RUN pip install mitmproxy flask

WORKDIR /app

# Копируем аддон и скрипт для пинга
COPY addon.py /app/addon.py
COPY ping_server.py /app/ping_server.py

# Открываем порты
EXPOSE 8080 8081

# Запускаем оба сервиса
CMD ["sh", "-c", "python3 /app/ping_server.py & mitmdump -p 8080 -s /app/addon.py"]
