#Multithreading:execute parallel
from threading import Thread
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            print('Hello')
            sleep(1)
class Hii(Thread):
    def run(self):
        for i in range(5):
            print('Hi')
            sleep(1)

t1=Hello()
t2=Hii()

t1.start()
sleep(0.2)
t2.start()


#join()-used to stop the main thread execution
t1.join()
t2.join()

#main thread is responsible to print bye
print('bye')