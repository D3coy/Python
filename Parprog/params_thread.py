from threading import Thread
import time

class MyThread(Thread):
    def __init__(self, name, delay):
        #Thread.__init__(self)   # give initializer of [Thread:init <- self] of the current class to fill
        super().__init__()
        self.name = name
        self.delay = delay

    # redefinition of default run()
    def run(self):
        print("Starting thread {}.".format(self.name))
        thread_count_down(self.name, self.delay)
        print("Finished thread {}.".format(self.name))

def thread_count_down(name, delay):
    counter = 5

    while counter:
        time.sleep(delay)
        print("Thread %s counting down: %i..." % (name, counter))
        counter -= 1

# absent exec string (maybe a race condition in 22 row)
MyThread(name= "[t1]", delay= 5).start()    # start() -> run()
MyThread(name= "[t2]", delay= 5).start()