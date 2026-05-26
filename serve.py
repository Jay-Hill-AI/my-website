#!/usr/bin/env python3
"""Minimal static file server using only absolute paths — no getcwd() calls."""
import http.server, os, sys

ROOT = "/Users/Jaume/Documents/MrRobot/my-website"
PORT = 8080

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)
    def log_message(self, fmt, *args):
        pass  # suppress request logs

os.chdir(ROOT)  # set cwd explicitly before server starts
with http.server.HTTPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
