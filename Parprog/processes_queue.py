from multiprocessing import Queue, Process      # special queue for processes only
import random

def func(q):
    q.put([42, None, "world"])

def main():
    q = Queue()     # q initializer
    proc = Process(target= func, args= (q, ))       # p init
    proc.start()

    print(q.get())      # get data from <put()> data in queue FIFO pipe

if __name__ == "__main__":
    main()