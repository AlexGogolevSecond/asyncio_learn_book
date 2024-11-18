from asyncio import Future
import asyncio


# # Получаем текущий цикл событий
# loop = asyncio.get_event_loop()
# if loop.is_running():
#     # Если цикл событий уже запущен, используем его
#     my_future = loop.create_future()
# else:
#     # Если нет, создаем новый цикл событий
#     my_future = asyncio.Future()


my_future = Future()

print(f'Is my_future done? {my_future.done()}')

my_future.set_result(42)

print(f'Is my_future done? {my_future.done()}')
print(f'What is the result of my_future? {my_future.result()}')
