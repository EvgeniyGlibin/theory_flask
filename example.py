from datetime import datetime

def app(environ, start_responce):
    time = datetime.now()
    data = bytes(f'The time is {time:%b %d %H:%M:%S}', 'utf-8')
    start_responce("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return [data]