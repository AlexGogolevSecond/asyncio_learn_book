async def application(scope, receive, send):
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [[b'content-type', b'text/html']]
    })
    await send({'type': 'http.response.body', 'body': b'ASGI hello!'})

# запуск uvicorn chapter_09.listing_9_7:application

# напрямую uvicorn не рекомендуется запускать - рекомендуется запускать uvicorn с помощью gunicorn,
# т.к. в Gunicorn встроена логика автоматического перезапуска рабочих процессов в случае аварии
