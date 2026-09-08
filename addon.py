from mitmproxy import http
import re

def response(flow: http.HTTPFlow) -> None:
    if "nz.ua" not in flow.request.pretty_host:
        return

    target_paths = ["/grades/", "/marks/", "/profile"]
    if not any(path in flow.request.path for path in target_paths):
        return

    if flow.response and flow.response.text:
        original = flow.response.text
        modified = re.sub(r'\b([1-9][0-9]?|100)\b', '100', original)
        if modified != original:
            flow.response.text = modified
            print(f"[*] Подмена выполнена для {flow.request.path}")
