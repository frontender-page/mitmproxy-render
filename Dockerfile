FROM python:3.10-slim

RUN pip install mitmproxy

WORKDIR /app

COPY addon.py /app/addon.py

EXPOSE 8080

# Явно указываем режим regular и добавляем флаг для обработки CONNECT
CMD ["mitmdump", "-p", "8080", "-s", "/app/addon.py", "--mode", "regular", "--ssl-insecure"]
