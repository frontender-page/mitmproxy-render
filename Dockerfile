FROM python:3.10-slim

# Устанавливаем mitmproxy и Flask
RUN pip install mitmproxy flask

WORKDIR /app
 
# Копируем файлы
COPY addon.py /app/addon.py
COPY ping_server.py /app/ping_server.py

# Открываем порты
EXPOSE 8080
EXPOSE 8081

# Запускаем оба сервиса через обёртку
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

CMD ["/app/start.sh"]
