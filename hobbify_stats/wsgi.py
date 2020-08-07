#!/usr/bin/env python
"""This script contains the codes to start the wsgi server"""
from server import app

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
