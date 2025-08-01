from concurrent.futures import ThreadPoolExecutor
from time import sleep



def долгая_операция(x):
    sleep(3)
    return x * x

# Создаем пул потоков
with ThreadPoolExecutor() as executor:
    # Запускаем операцию в отдельном потоке и получаем Future
    future = executor.submit(долгая_операция, 555555555555)

    # Проверяем, готов ли результат
    if future.done():
        print("Результат готов!")
    else:
        print("Еще выполняется...")

    # Получаем результат (если не готов, программа будет ждать)
    result = future.result()
    print(result)  # 25
