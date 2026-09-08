#!/bin/sh
python3 /app/ping_server.py &
mitmdump -p 8080 -s /app/addon.py
