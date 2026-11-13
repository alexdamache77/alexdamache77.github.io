#!/usr/bin/env python3
"""
Run this from the portfolio folder:
    python3 preview.py

Then open http://localhost:8000 in your browser.
All images load instantly — no Vercel needed.
Press Ctrl+C to stop.
"""
import http.server, webbrowser, threading, os

PORT = 8000
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass  # silence request logs

def open_browser():
    import time; time.sleep(0.4)
    webbrowser.open(f'http://localhost:{PORT}')

threading.Thread(target=open_browser, daemon=True).start()
print(f'Preview running at http://localhost:{PORT}')
print('Press Ctrl+C to stop.')
http.server.HTTPServer(('', PORT), Handler).serve_forever()
