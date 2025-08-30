import socket
import threading
import time

def client_thread(client_id, message, num_requests=10):
    """Функция для каждого клиентского потока"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect(('127.0.0.1', 8000))

            for i in range(num_requests):
                # Отправляем сообщение
                msg = f"Client {client_id}: {message} - {i+1}"
                client.sendall(msg.encode('utf-8'))
                print(f"Client {client_id} sent: {msg}")

                # Получаем ответ
                response = client.recv(2048)
                print(f"Client {client_id} received: {response.decode('utf-8')}")

                time.sleep(0.1)  # Небольшая задержка

    except Exception as e:
        print(f"Client {client_id} error: {e}")

# Запуск нескольких клиентов одновременно
def test_multiple_clients():
    threads = []
    num_clients = 5  # Количество одновременных клиентов
    messages = ["Hello", "Test", "Echo", "Multi", "Thread"]

    for i in range(num_clients):
        thread = threading.Thread(
            target=client_thread, 
            args=(i, messages[i], 3)  # 3 запроса на клиента
        )
        threads.append(thread)
        thread.start()

    # Ждем завершения всех потоков
    for thread in threads:
        thread.join()

    print("All clients completed")

if __name__ == "__main__":
    test_multiple_clients()
