import asyncio
from concurrent.futures import ProcessPoolExecutor

# Важно: функция должна быть определена на верхнем уровне модуля
# (не внутри другой функции/класса) для ProcessPoolExecutor
def cpu_intensive_task(n):
    return sum(i * i for i in range(n))

async def main():
    loop = asyncio.get_running_loop()

    # Важно: создавать Executor внутри асинхронной функции,
    # но лучше использовать контекстный менеджер
    try:
        with ProcessPoolExecutor() as pool:
            result = await loop.run_in_executor(
                pool,
                cpu_intensive_task,
                10_000_000
            )
            print(f"Результат: {result}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Важно: защитить точку входа для многопроцессорных приложений
if __name__ == "__main__":
    asyncio.run(main())
