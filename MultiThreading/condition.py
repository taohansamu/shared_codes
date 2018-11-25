import random
import threading
import time


class Producer(threading.Thread):
    """
    Producers random integers to a list
    """

    def __init__(self, integers, condition):
        threading.Thread.__init__(self)
        self.name = 'Producer'
        self.integers = integers
        self.condition = condition

    def run(self):
        """
        Append random integers to integers list at random time.
        """
        while True:
            integer = random.randint(0, 256)
            self.condition.acquire()
            print('condition acquired by {}'.format(self.name))
            self.integers.append(integer)
            print('{} appended to list by {}'.format(integer, self.name))

            print('condition notified by {}'.format(self.name))
            self.condition.notify()

            print('condition released by {}'.format(self.name))
            self.condition.release()
            time.sleep(1)


class Consumer(threading.Thread):
    """
        consumes random integers for a list
    """

    def __init__(self, integers, condition):
        threading.Thread.__init__(self)
        self.name = 'Consumer'
        self.integers = integers
        self.condition = condition

    def run(self):
        """
        Consumes integers from shared list
        """
        while True:
            self.condition.acquire()
            print('condition acquired by {}'.format(self.name))
            while True:
                if self.integers:
                    integer = self.integers.pop()
                    print('{} popped from list by {}'.format(integer, self.name))
                    break
                    print('conditon wait by {}'.format(self.name))
            self.condition.wait()
            print('condition released by {}'.format(self.name))
            self.condition.release()


def main():
    integers = []
    condition = threading.Condition()
    producer = Producer(integers, condition)
    consumer = Consumer(integers, condition)
    producer.start()
    consumer.start()

    producer.join()
    consumer.join()


if __name__ == '__main__':
    main()