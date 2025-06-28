import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создать TCP-сервер
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = ('127.0.0.1', 15454)  # задаём адрес сокета
server_socket.bind(server_address)
server_socket.listen()

connection, client_address = server_socket.accept()
print(f'Получен запрос на подключение от {client_address}!')
