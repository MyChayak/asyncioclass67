import time
import asyncio
from asyncio import Queue

# Product and Customer classes
class Product:
    def __init__(self, product_name: str, checkout_time: float):
        self.product_name = product_name
        self.checkout_time = checkout_time

class Customer:
    def __init__(self, customer_id: int, products: list[Product]):
        self.customer_id = customer_id
        self.products = products

# Checkout function (consumer)
async def checkout_customer(queue: Queue, cashier_number: int):
    cashier_take = {'id': cashier_number, 'customer': 0, 'time': 0}
    while not queue.empty():
        customer: Customer = await queue.get()
        cashier_take['customer'] += 1
        customer_start_time = time.perf_counter()
        print(f"The Cashier_{cashier_number} "
              f"will checkout Customer_{customer.customer_id}")
        
        for product in customer.products:
            if cashier_number == 2 :
                product_take_time = 0.1
            else:
                product_take_time = round(product.checkout_time + (0.1*cashier_number), 2)

        for product in customer.products:
            product_take_time = round(product.checkout_time, ndigits=2)
            print(f"The Cashier_{cashier_number} "
                  f"will checkout Customer_{customer.customer_id}'s "
                  f"Product_{product.product_name} "
                  f"in {product.checkout_time} secs")
            await asyncio.sleep(product.checkout_time)
            cashier_take['time'] += product_take_time

        print(f"The Cashier_{cashier_number} "
              f"finished checkout Customer_{customer.customer_id} "
              f"in {round(time.perf_counter() - customer_start_time, ndigits=2)} secs")
        
        queue.task_done()
    return cashier_take

# Customer generation (producer)
def generate_customer(customer_id: int) -> Customer:
    all_products = [Product('beef', 1),
                    Product('banana', .4),
                    Product('sausage', .4),
                    Product('diapers', .2)]
    return Customer(customer_id, all_products)

async def customer_generation(queue: Queue, customers: int):
    customer_count = 0
    while True:
        customers = [generate_customer(the_id)
                     for the_id in range(customer_count, customer_count + customers)]
        
        for customer in customers:
            print("Waiting to put customer in line...")
            await queue.put(customer)
            print("Customer put in line...")
        
        customer_count = customer_count + len(customers)
        await asyncio.sleep(0.001)
        return customer_count

# Main function
async def main():
    CUSTOMER = 2
    QUEUE_SIZE = 2
    CASHIER = 2
    customer_queue = Queue(QUEUE_SIZE)
    customer_start_time = time.perf_counter()
    
    async with asyncio.TaskGroup() as group:
        customer_group = group.create_task(customer_generation(customer_queue, CUSTOMER))
        cashiers_group = [group.create_task(checkout_customer(customer_queue, i)) for i in range(CASHIER)]
    
    for cg in cashiers_group:
        if cg.result():
            cashier = cg.result()
            print(f"The Cashier_{cashier['id']} "
                  f"take {cashier['customer']} customers "
                  f"total {round(cashier['time'], ndigits=2)} secs.")

    if customer_group.result() :      
        print(f"\n"
              f"The supermarket process finished "
              f"{customer_group.result()} customers "
              f"in {round(time.perf_counter() - customer_start_time, ndigits=2)} secs.")
                
    # Wait for the queue to be emptied and stop cashiers
    # await customer_queue.join()
    # for _ in range(CASHIER):
    #     await customer_queue.put(None)  # Sentinel to stop cashiers

if __name__ == "__main__":
    asyncio.run(main())
