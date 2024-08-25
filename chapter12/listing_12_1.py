import asyncio
from asyncio import Queue
from random import randrange
from typing import List


class Product:
    def __init__(self, name: str, checkout_time: float):
        self.name = name
        self.checkout_time = checkout_time


class Customer:
    def __init__(self, customer_id: int, products: List[Product]):
        self.customer_id = customer_id
        self.products = products


async def checkout_customer(queue: Queue, cashier_number: int):
    while not queue.empty(): #A
        customer: Customer = queue.get_nowait()  # задача (кассир) получает покупателя из очереди
        print(f'Кассир {cashier_number} начал обслуживать покупателя {customer.customer_id} ({len(customer.products)} продукта)')
        for product in customer.products: #B
            print(f"Кассир {cashier_number} обслуживает покупателя {customer.customer_id}'s {product.name}")
            await asyncio.sleep(product.checkout_time)
        print(f'Кассир {cashier_number} закончил обслуживать покупателя {customer.customer_id}')
        queue.task_done()  # сигнализирует очереди, что исполнитель завершил обработку текущего элемента данных


async def main():
    customer_queue = Queue()

    all_products = [Product('пиво', 2),
                    Product('бананы', .5),
                    Product('колбаса', .2),
                    Product('подгузники', .2)]

    for i in range(10): #C  вставляем в очередь n покупателей и их покупки
        products = [all_products[randrange(len(all_products))] for _ in range(randrange(10))]  # генерим рандомный список продуктов в корзине
        customer_queue.put_nowait(Customer(i, products))  # вставляем объект покупателя с его покупками в очередь

    cashiers = [asyncio.create_task(checkout_customer(customer_queue, j)) for j in range(3)]  # 3 кассира обрабатывают очередь из 10 покупателей

    await asyncio.gather(customer_queue.join(), *cashiers)  # ??? что за join ?

asyncio.run(main())
