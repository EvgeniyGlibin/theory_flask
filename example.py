def app(environ, start_responce):
    data = b"Hello, World!\n"
    start_responce("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])