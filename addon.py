from mitmproxy import http
import re

# --- ОБРАБОТЧИК ЗАПРОСОВ ---
def request(flow: http.HTTPFlow) -> None:
    # 1. Обработка /ping для Cron-job
    if flow.request.path == "/ping":
        flow.response = http.Response.make(200, b"pong", {"Content-Type": "text/plain"})
        return

    # 2. Логирование CONNECT-запросов (для отладки)
    if flow.request.method == "CONNECT":
        print(f"[CONNECT] {flow.request.host}:{flow.request.port}")

# --- ОБРАБОТЧИК ОТВЕТОВ (ПОДМЕНА ОЦЕНОК) ---
def response(flow: http.HTTPFlow) -> None:
    # Проверяем, что запрос идёт к nz.ua
    if "nz.ua" not in flow.request.pretty_host:
        return

    # Проверяем URL-путь — подменяем только страницы с оценками
    target_paths = ["/grades/", "/marks/", "/profile", "/dashboard/news"]
    if not any(path in flow.request.path for path in target_paths):
        return

    # Если ответ содержит текст — выполняем замену
    if flow.response and flow.response.text:
        original = flow.response.text

        # --- ПРИМЕРЫ ПОДМЕНЫ ---
        # 1. Все числа от 1 до 100 → 100
        modified = re.sub(r'\b([1-9][0-9]?|100)\b', '100', original)

        # 2. Конкретные JSON-поля (раскомментируйте при необходимости)
        # modified = modified.replace('"score": 45', '"score": 95')
        # modified = modified.replace('"grade": "B"', '"grade": "A"')

        # Если изменения есть — применяем их
        if modified != original:
            flow.response.text = modified
            print(f"[*] Подмена выполнена для {flow.request.path}")
