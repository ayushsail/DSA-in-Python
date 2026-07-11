from Data_Structure.Linear.A8QueueImplementation import QueueLL
'''
(1) For all exercises use Queue class implemented in main tutorial.
Design a food ordering system where your python program will run two threads,
Place Order: This thread will be placing an order and inserting that into a queue. 
This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)

Serve Order: This thread will server the order. 
All you need to do is pop the order out of the queue and print it.
This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.
'''

