import thread
import threading


def target_func(x):
    print('{} thread has id: {}'.format(x, thread.get_ident()))


class WorkerThread(threading.Thread):
    def __init__(self, data):
        threading.Thread.__init__(self)
        self.data = data

    def run(self):
        print('{} thread has id: {}'.format(self.ident, self.data))


if __name__ == '__main__':
    a = 'thread 1'
    b = 'thread 2'
    thread1 = threading.Thread(target = target_func, args=(a,))
    thread2 = WorkerThread(b)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print('Main thread exited')