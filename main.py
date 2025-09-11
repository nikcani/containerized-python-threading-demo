import threading
import time
import queue

# Create a queue to act as the communication channel between threads
data_queue = queue.Queue()


def producer_thread():
    """
    This thread produces data and puts it into the queue.
    """
    print("Producer thread: starting.")
    for i in range(5):
        message = f"Message number {i}"
        print(f"Producer thread: putting '{message}' into the queue.")
        data_queue.put(message)
        time.sleep(1)  # Simulate some work
    data_queue.put(None)  # Sentinel value to signal the end of data
    print("Producer thread: finished.")


def consumer_thread():
    """
    This thread consumes data from the queue.
    """
    print("Consumer thread: starting.")
    while True:
        message = data_queue.get()
        if message is None:  # Check for the sentinel value
            print("Consumer thread: received termination signal.")
            break
        print(f"Consumer thread: received '{message}' from the queue.")
        time.sleep(1.5)  # Simulate some processing
    print("Consumer thread: finished.")


if __name__ == "__main__":
    producer = threading.Thread(target=producer_thread)
    consumer = threading.Thread(target=consumer_thread)

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

    print("Main thread: all threads have completed.")
